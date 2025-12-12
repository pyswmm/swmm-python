from datetime import datetime, timedelta
import os
import pytest
from swmm.toolkit import solver, output, shared_enum

DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
INPUT_FILE = os.path.join(DATA_PATH, "test_Example1.inp")
REPORT_FILE = os.path.join(DATA_PATH, "temp_align.rpt")
OUTPUT_FILE = os.path.join(DATA_PATH, "temp_align.out")

REPORT_STEP_SECONDS = 3600  # Example1


def cdd(t, r):
    import math

    if t == r:
        return 10.0

    tmp = abs(t - r)
    if tmp < 1.0e-7:
        tmp = 1.0e-7
    elif tmp > 2.0:
        tmp = 1.0

    tmp = -math.log10(tmp)
    if tmp < 0.0:
        tmp = 0.0

    return tmp

def check_cdd_float(test: list[float], ref: list[float], cdd_tol: int) -> bool:
    """
    Checks minimum correct decimal digits between two float sequences. Fails if lengths differ.
    """
    import math

    if len(test) != len(ref):
        return False
    
    min_cdd = 10.0

    for t, r in zip(test, ref):
        tmp = cdd(t, r)

        if tmp < min_cdd:
            min_cdd = tmp

    return math.floor(min_cdd) >= cdd_tol


def _curr_dt():
    y, m, d, hh, mm, ss = solver.simulation_get_current_datetime()
    return datetime(y, m, d, hh, mm, ss)

def build_link_flow_solver_tuples_aligned():
    tuples = []
    solver.swmm_open(INPUT_FILE, REPORT_FILE, OUTPUT_FILE)
    try:
        solver.swmm_start(0)
        # After start callback
        # period_end = _curr_dt()
        # value = solver.link_get_result(0, shared_enum.LinkResult.FLOW)
        # tuples.append((period_end, value))

        while True:
            # Before step callback
            #
            time_left = solver.swmm_stride(REPORT_STEP_SECONDS)
            # After step callback
            #
            if time_left == 0:
                break
            # Value for the interval that just ended; align to its period-end timestamp
            period_end = _curr_dt() - timedelta(seconds=REPORT_STEP_SECONDS)
            value = solver.link_get_result(0, shared_enum.LinkResult.FLOW)
            tuples.append((period_end, value))

        # Before end callback
        period_end = _curr_dt() - timedelta(seconds=REPORT_STEP_SECONDS)
        value = solver.link_get_result(0, shared_enum.LinkResult.FLOW)
        tuples.append((period_end, value))

        solver.swmm_end()
        # After end callback
        #

    finally:
        solver.swmm_close()
        # After close callback
        #
    return tuples

def build_link_flow_output_tuples():
    EPOCH_SWMM = datetime(1899, 12, 30)
    h = output.init()
    output.open(h, os.path.join(DATA_PATH, "test_Example1.out"))
    try:
        start_days = output.get_start_date(h)
        rpt = output.get_times(h, shared_enum.Time.REPORT_STEP)
        n = output.get_times(h, shared_enum.Time.NUM_PERIODS)
        start_dt = EPOCH_SWMM + timedelta(days=start_days)
        vals = output.get_link_series(h, 0, shared_enum.LinkAttribute.FLOW_RATE, 0, n - 1)
        tuples = [(start_dt + timedelta(seconds=i * rpt), float(vals[i])) for i in range(n)]
    finally:
        output.close(h)
    return tuples

def test_compare_aligned_series():
    s = build_link_flow_solver_tuples_aligned()
    o = build_link_flow_output_tuples()

    # times must match
    solver_times = [t.strftime("%Y-%m-%d %H:%M:%S") for t, _ in s]
    output_times = [t.strftime("%Y-%m-%d %H:%M:%S") for t, _ in o]
    assert solver_times == output_times, (
        "Time axes differ.\n"
        f"Solver times: {solver_times[:5]} ...\n"
        f"Output times: {output_times[:5]} ..."
    )

    # values should match within tolerance
    solver_vals = [v for _, v in s]
    output_vals = [v for _, v in o]

    assert check_cdd_float(solver_vals, output_vals, 1), (
        "Solver and output values differ. "
        "See zipped output for details:\n" +
        "\n".join(
            f"{t1.strftime('%Y-%m-%d %H:%M:%S')} | {v1:.6f} || {t2.strftime('%Y-%m-%d %H:%M:%S')} | {v2:.6f} | cdd={cdd(v1, v2):.2f}"
            for (t1, v1), (t2, v2) in list(zip(s, o))[:10]
        )
    )


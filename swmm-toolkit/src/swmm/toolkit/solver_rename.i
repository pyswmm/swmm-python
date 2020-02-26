/*
 *  solver_rename.i - Rename mapping for swmm-solver
 *
 *  Created:    2/26/2020
 *
 *  Author:     Michael E. Tryby
 *              US EPA - ORD/CESER
 *
*/


// RENAME FUNCTIONS ACCORDING TO PEP8
%rename(run)                swmm_run;
%rename(open)               swmm_open;
%rename(start)              swmm_start;
%rename(step)               swmm_step;
%rename(end)                swmm_end;
%rename(report)             swmm_report;
%rename(get_mass_bal_err)   swmm_getMassBalErr;
%rename(close)              swmm_close;
%rename(get_version)        swmm_getVersion;

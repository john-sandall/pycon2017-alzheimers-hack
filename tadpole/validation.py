import numpy as np


def get_test_subjects(LB_Table):
    """Load test subjects in LB2 cohort

    :param LB_Table: Feature matrix
    :type LB_Table: pd.DataFrame
    :return: Unique list of patient identifiers
    :rtype: np.ndarray
    """
    # * Copy the column specifying membership of LB2 into an array.
    LB2_inds = LB_Table['RID'][LB_Table.LB2 == 1]

    # * Get the list of subjects to forecast from LB2 - the ordering is the
    # * same as in the submission template.
    return np.unique(LB2_inds)

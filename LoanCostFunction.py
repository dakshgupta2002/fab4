def loan_cost_prediction(revenue,
                         profit_percentage_last_year,
                         simple_interest,
                         interest_rate,
                         amount_of_loan,
                         time_to_repay,
                         past_debt_to_repay,
                         sustainability,
                         competition_scale,
                         management_effectivity,
                         startup,
                         cibil_score,
                         inflation=4):

    # balance the decrease in amount of money
    interest_rate -= inflation

    # substract from the net revenue
    external_cost = (pow(10, len(str(amount_of_loan))-2))*(
        5*(1-sustainability) +
        3*(1-management_effectivity) +
        2*(startup) +
        10*(900 - cibil_score)/100 +
        3*(competition_scale)
    )

    loan_interest_cost = amount_of_loan * \
        (1+interest_rate*time_to_repay) if simple_interest else amount_of_loan * \
        (pow((1 + interest_rate/100), time_to_repay))

    # the net profit conceded over the period of time
    net_revenue = revenue*profit_percentage_last_year*time_to_repay/100

    # print(external_cost, loan_interest_cost, net_revenue)

    residue_left_after_time = net_revenue - external_cost - \
        loan_interest_cost - past_debt_to_repay

    # print(residue_left_after_time)

    if residue_left_after_time <= 0:
        if abs(residue_left_after_time) > 0.5*net_revenue*profit_percentage_last_year/100:
            return -2  # High Loss
        else:
            return -1  # small loss
    else:
        if (residue_left_after_time) < 0.5*net_revenue*profit_percentage_last_year/100:
            return 1  # small profit
        else:
            return 2  # high profit
        

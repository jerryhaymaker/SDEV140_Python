def main():
    FOR_EACH_DAY = [ "Monday", "Tuesday", "Wednesday", "Thursday",\
                   "Friday", "Saturday", "Sunday"]
    SALE_OF_DAY = INPUT_DAILY_SALES(FOR_EACH_DAY)
    TOTAL_DAILY_SALE = CALC_WEEK_SALE(SALE_OF_DAY)
    DISPLAY_REPORT(FOR_EACH_DAY, SALE_OF_DAY, TOTAL_DAILY_SALE)
def INPUT_DAILY_SALES(FOR_EACH_DAY):
    SALE_OF_DAY = []
    for CURRENT_DAY in FOR_EACH_DAY:
        print("Plese enter sales for", CURRENT_DAY + ": ", end = "")
        DAILY_SALE = float(input())
        SALE_OF_DAY.append(DAILY_SALE)
    return SALE_OF_DAY
def CALC_WEEK_SALE(SALE_OF_DAY):
    TOTAL = 0
    for CURRENT_DAY_SALE in range(len(SALE_OF_DAY)):
        TOTAL = TOTAL + SALE_OF_DAY[CURRENT_DAY_SALE]
    return TOTAL
def DISPLAY_REPORT(FOR_EACH_DAY, SALE_OF_DAY, TOTAL_SALES):
    print("\nSALES REPORT\n")
    for CURRENT_DAY in range(len(FOR_EACH_DAY)):
        print(FOR_EACH_DAY[CURRENT_DAY]+"'s sales: ",\
              "$" + format(SALE_OF_DAY[CURRENT_DAY], ".2f"))
        print("\nTotal weeklySales: ", "$" + format(TOTAL_SALES, ".2f"))
main()

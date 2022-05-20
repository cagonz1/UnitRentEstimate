print("Enhanced Voucher URE for the Ridgecrest Community.")
print()

# ---user entered data ---

# bedroom size              =       bedSiz
# gross annual income       =       groAnnInc
# annual adjusted income    =       annAdjInc
# choose the currently
# used utility allowance
# table or else the unit
# is all bills paid         =       utilAll
# rent to owner             =       renToOwn
# current rent to owner     =       curRenToOwn

bedSiz = int(input("Please enter the number of bedrooms.\n"))
groAnnInc = int(input("Please enter the Gross Annual Income for the resident.\n"))
annAdjInc = int(input("Please enter the residents Annual Adjusted Income.\n"))
utilAll = input("Do you want to use the utility allowance schedule \"2021 Flat Utility Allowance\"?\n"
                "Enter \"Y\" or \"N\"\n").lower()
# use a try except here to validate the entry for utilAll
renToOwn = int(input("Please enter the Rent to Owner.\n"))
# the current rent to owner or the current tenant rent
curRenToOwn = int(input("What is the Current Tenant Rent? \n"))

# ---variable assignment---

MinRent = 50
ua = 0
pmtStd = 0

# ---functions---

# utility allowance        =    uta()
# payment standard         =    ps()


def uta():
    global ua
    if utilAll == "n":
        ua = 0
    elif bedSiz == 0:
        ua = 77
    elif bedSiz == 1:
        ua = 97
    elif bedSiz == 2:
        ua = 129
    elif bedSiz == 3:
        ua = 184
    elif bedSiz == 4:
        ua = 218
    elif bedSiz == 5:
        ua = 283
    elif bedSiz == 6:
        ua = 296
    return ua


def pys():
    global pmtStd
    if bedSiz == 0:
        pmtStd = 930
    elif bedSiz == 1:
        pmtStd = 1100
    elif bedSiz == 2:
        pmtStd = 1330
    elif bedSiz == 3:
        pmtStd = 1710
    elif bedSiz == 4:
        pmtStd = 2110
    elif bedSiz == 5:
        pmtStd = 2427
    elif bedSiz == 6:
        pmtStd = 2743
    return pmtStd


# ---variable assignment from calculations---

# monthly adjusted income               =   monAdjInc
# 30% of their annual adjusted income   =   thrPerAnnAdjInc
# 10% gross annual income               =   tnPerGroAnnInc
# gross rent                            =   grRnt
# total tenant portion                  =   ttp
# total voucher subsidy                 =   totVcrSub
# total family share                    =   totFamShr
# hap to owner                          =   haToOwn
# family contribution                   =   famCont
# utility allowance reimbursement       =   utAllRe
# max family contribution               =   maFamCon

monAdjInc = round(annAdjInc / 12)
thrPerAnnAdjInc = round((annAdjInc / 12) * .3)
tnPerGroAnnInc = round((groAnnInc / 12) * .1)
grRnt = renToOwn + uta()
ttp = max(thrPerAnnAdjInc, tnPerGroAnnInc, MinRent, curRenToOwn)
totVcrSub = max(0, (grRnt - ttp))
totFamShr = monAdjInc * .4

if totVcrSub > renToOwn:
    haToOwn = renToOwn
else:
    haToOwn = totVcrSub

famCont = renToOwn - haToOwn
utAllRe = totVcrSub - haToOwn

if annAdjInc == 0:
    maFamCon = 0
else:
    maFamCon = round((annAdjInc / 12) * .4)

# ---results---

print(f"bedroom size:                        {type(bedSiz)},{bedSiz}")
print(f"gross annual income:                 {type(groAnnInc)},{groAnnInc}")
print(f"annual adjusted income:              {type(annAdjInc)},{annAdjInc}")
print(f"using the flat ua fee schedule:      {type(utilAll)},{utilAll}")
print(f"rent to owner:                       {type(renToOwn)},{renToOwn}")
print(f"current rent to owner:               {type(curRenToOwn)},{curRenToOwn}")
print(f"monthly adjusted income:             {type(monAdjInc)},{monAdjInc}")
print(f"30% of their annual adjusted income: {type(thrPerAnnAdjInc)},{thrPerAnnAdjInc}")
print(f"10% gross annual income:             {type(tnPerGroAnnInc)},{tnPerGroAnnInc}")
print(f"gross rent:                          {type(grRnt)},{grRnt}")
print(f"total tenant portion:                {type(ttp)},{ttp}")
print(f"total voucher subsidy:               {type(totVcrSub)},{totVcrSub}")
print(f"total family share:                  {type(totFamShr)},{totFamShr}")
print(f"hap to owner:                        {type(haToOwn)},{haToOwn}")
print(f"family contribution:                 {type(famCont)},{famCont}")
print(f"utility allowance reimbursement:     {type(utAllRe)},{utAllRe}")
print(f"max family contribution:             {type(maFamCon)},{maFamCon}")
print(f"payment standard:                    {type(pys())},{pys()}")
print(f"Utility Allowance:                   {type(uta())},{uta()}")


# need to be able to save every calculation into a database for analysis later as well as audit trail
# the user, date and time stamp, entries

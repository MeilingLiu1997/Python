Base_premium = 100

age = int(input("Please enter your age: "))
el = input("Bachelor or Master? ")
ms = input("Are you married? (yes/no)")
es = input("Student or unemployed?")

if age <= 22 or age >= 70:
    InsuranceAge = Base_premium * (1 + 0.25)

    if el == 'bachelor':
        insuranceElb = InsuranceAge * (1 - 0.1)

        if ms == "yes":
            insuranceMs = insuranceElb * (1 - 0.2)

            if es == "student":
                insuranceEs = insuranceMs * (1 + 0.1)
                print("Your Monthly Insurance: $", format(insuranceEs, '.1f'))
            else:
                insuranceEs = insuranceMs * (1 - 0.05)
                print("Your Monthly Insurance: $", insuranceEs)
        else:
            if ms == 'no':
                insuranceMs = insuranceElb

                if es == "student":
                    insuranceEs = insuranceMs * (1 + 0.1)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
                else:
                    insuranceEs = insuranceMs * (1 - 0.05)
                    print("Your Monthly Insurance: $", insuranceEs)
    else:
        if el == 'master':
            insuranceElm = InsuranceAge * (1 - 0.2)

            if ms == "yes":
                insuranceMs = insuranceElm * (1 - 0.2)

                if es == "student":
                    insuranceEs = insuranceMs * (1 + 0.1)
                    print("Your Monthly Insurance: $", insuranceEs)
                else:
                    insuranceEs = insuranceMs * (1 - 0.05)
                    print("Your Monthly Insurance: $", insuranceEs)
            else:
                insuranceMs = insuranceElm

                if es == "student":
                    insuranceEs = insuranceMs * (1 + 0.1)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
                else:
                    insuranceEs = insuranceMs * (1 - 0.05)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))

else:
    InsuranceAge = Base_premium

    if el == 'bachelor':
        insuranceElb = InsuranceAge * (1 - 0.1)

        if ms == "yes":
            insuranceMs = insuranceElb * (1 - 0.2)

            if es == "student":
                insuranceEs = insuranceMs * (1 + 0.1)
                print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
            else:
                insuranceEs = insuranceMs * (1 - 0.05)
                print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
        else:
            if ms == 'no':
                insuranceMs = insuranceElb

                if es == "student":
                    insuranceEs = insuranceMs * (1 + 0.1)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
                else:
                    insuranceEs = insuranceMs * (1 - 0.05)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
    else:
        if el == 'master':
            insuranceElm = InsuranceAge * (1 - 0.2)

            if ms == "yes":
                insuranceMs = insuranceElm * (1 - 0.2)

                if es == "student":
                    insuranceEs = insuranceMs * (1 + 0.1)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
                else:
                    insuranceEs = insuranceMs * (1 - 0.05)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))

            else:
                insuranceMs = insuranceElm

                if es == "student":
                    insuranceEs = insuranceMs * (1 + 0.1)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
                else:
                    insuranceEs = insuranceMs * (1 - 0.05)
                    print("Your Monthly Insurance: $", format(insuranceEs, '.2f'))
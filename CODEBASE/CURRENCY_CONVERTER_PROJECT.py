Exchange_rates={
    "INR":1,   #Indian Rupee
    "USD":83,  #United States Dollar
    "EUR":90,  #Euro
    "GBP":105  #British Pound
}

#Function to convert currency into INR
def convert_to_inr(amount,currency):
    result=amount * Exchange_rates[currency] 
    return result

#Function to convert into respective currency
def convert_currency():
    print("============CURRENCY CONVERTER============")
    print("Available Currencies are:")
    print("INR (Indian Rupees)")
    print("USD (United States Dollar)")
    print("EUR (Euro)")
    print("GBP (British Pound)")
    
    # Taking amount from the user
    try:
        Amount = float(input("Enter amount:"))

    except ValueError:
        print("Entered amount is invalid. Please enter a valid amount.")
    return

    # Checking negative amount 

    if Amount < 0:
        print("Amount cannot be negative")
    return

    #Taking input from the user
    currency_from=input("Convert from following: INR, USD, EUR, GBP").strip().upper()
    

    currency_to=input("Convert to following: INR, USD, EUR, GBP").strip().upper()
   


    #Checking Currency codes

    if currency_from not in Exchange_rates:
        print("Sorry! This currency is not available for conversion")
        return

    if currency_to not in Exchange_rates:
        print("Sorry! This currency is not available for conversion")
        return


    #Step:1 Convert currency into INR
    amount_in_inr=convert_to_inr(Amount, currency_from)

    #Step:2 Convert INR into respective currency
    converted_amount= amount_in_inr/Exchange_rates[currency_to]



    #Display the result
    print(f"\n{Amount} {currency_from} = "
          f"{converted_amount:.2f} {currency_to}")
    

#Calling the main function:

if __name__ == "__main__":
    convert_currency()
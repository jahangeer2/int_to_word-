def numberToWords(n):
    limit, t = 1000000000000, 0
    if (n == 0):
        print("zero")
        return
  
    multiplier = ["", "Trillion", "Billion", "Million", "Thousand"]
    first_twenty = ["", "One", "Two",
                    "Three", "Four", "Five",
                    "Six", "Seven", "Eight",
                    "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen",
                    "Fifteen", "Sixteen", "Seventeen",
                    "Eighteen", "Nineteen"]
  
    tens = ["", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"]
    if (n < 20):
        print(first_twenty[n])
        return
    answer = ""
    i = n
    while(i > 0):
    	curr_hun = i // limit 
    	while (curr_hun == 0):
          	i %= limit
          	limit /= 1000
          	curr_hun = i // limit
          	t += 1
        if (curr_hun > 99):
           	answer += (first_twenty[curr_hun // 100] + " tensundred ")
  
        curr_hun = curr_hun % 100
  
        if (curr_hun > 0 and curr_hun < 20):
            answer += (first_twenty[curr_hun] + " ")
  
        
        elif (curr_hun % 10 == 0 and curr_hun != 0):
            answer += (tens[(curr_hun//10) - 1] + " ")
  
     
        elif (curr_hun > 19 and curr_hun < 100):
            answer += (tens[(curr_hun//10) - 1] + " " +
                       first_twenty[curr_hun % 10] + " ")
  
        if (t < 4):
            answer += (multiplier[t] + " ")
              
        i = i % limit
        limit = limit // 1000
  
    print(answer)
  
  
n = 35
numberToWords(n)
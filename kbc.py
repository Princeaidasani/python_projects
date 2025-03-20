questions = [
  [
    "Which planet is known as the Red Planet?", 
    "Earth", "Mars", "Venus", "Jupiter", "None", 2
  ],
  [
    "Who is known as the Father of the Nation in India?", 
    "Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "Sardar Patel", "None", 2
  ],
  [
    "What is the capital of France?", 
    "Berlin", "Madrid", "Paris", "Rome", "None", 3
  ],
  [
    "Which is the largest animal in the world?", 
    "Elephant", "Blue Whale", "Giraffe", "Shark", "None", 2
  ],
  [
    "What is the primary source of energy for the Earth?", 
    "Moon", "Sun", "Stars", "Wind", "None", 2
  ],
  [
    "Which is the smallest continent in the world?", 
    "Asia", "Australia", "Europe", "Africa", "None", 2
  ],
  [
    "Who wrote the Indian national anthem?", 
    "Rabindranath Tagore", "Bankim Chandra Chatterjee", "Subhas Chandra Bose", "Mahatma Gandhi", "None", 1
  ],
  [
    "What is the boiling point of water in Celsius?", 
    "100°C", "0°C", "50°C", "200°C", "None", 1
  ],
  [
    "Which is the tallest mountain in the world?", 
    "K2", "Mount Everest", "Kangchenjunga", "Lhotse", "None", 2
  ],
  [
    "What is the national bird of India?", 
    "Peacock", "Sparrow", "Eagle", "Pigeon", "None", 1
  ],
  [
    "Which festival is known as the Festival of Lights in India?", 
    "Holi", "Diwali", "Eid", "Christmas", "None", 2
  ],
  [
    "How many colors are there in a rainbow?", 
    "5", "6", "7", "8", "None", 3
  ],
  [
    "What is the currency of the United States?", 
    "Euro", "Pound", "Dollar", "Yen", "None", 3
  ],
  [
    "Which ocean is the largest in the world?", 
    "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", "None", 4
  ],
  [
    "Which day is celebrated as International Yoga Day?", 
    "June 5", "June 21", "July 1", "August 15", "None", 2
  ],
  [
    "Which is the fastest land animal?", 
    "Lion", "Tiger", "Cheetah", "Leopard", "None", 3
  ],
  [
    "Which is the largest country in the world by area?", 
    "Canada", "China", "Russia", "USA", "None", 3
  ],
  [
    "Who was the first man to step on the moon?", 
    "Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "Rakesh Sharma", "None", 2
  ],
  [
    "Which is the longest river in the world?", 
    "Nile", "Amazon", "Yangtze", "Ganga", "None", 1
  ],
  [
    "Which sport is known as the 'Gentleman's Game'?", 
    "Football", "Tennis", "Cricket", "Hockey", "None", 3
  ],
  ]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000,2500000,5000000,10000000,70000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\nQuestion for Rs. {levels[i]}")
  print(f"{question[0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
    elif(i == 15):
      money = 70000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")
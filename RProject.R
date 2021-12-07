


blackjack <- function(decks, people){
  i <- people
  
  dec <- c("A","A","A","A",10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2)
  
  for(x in 1:i)
  {
    dec <- deal(dec) #updating deck with new deck after cards taken
  }
  return(1)
}

deal <- function(d){ #taking in deck and sending back deck after cards taken out
  
  index = sample(1:length(d), 2)
  hand = d[index]
  d = d[-index]
  
  print("Hand:") #printing hand
  print(hand)
  
  return(d)
}

  

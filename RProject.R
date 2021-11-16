
deal <- function(d){
  
  hand <- sample(d, 2, replace = FALSE) #choosing the 2 cards out of the deck
  paste(c("Hand is"), hand) #printing hand
  return(d)
}

blackjack <- function(decks, people){
  i <- people
  
  dec <- c("A","A","A","A",10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2)
  
  for(x in 0:i)
  {
    dec <- deal(dec) #updating deck with new deck after cards taken
  }
  return(1)
}



  

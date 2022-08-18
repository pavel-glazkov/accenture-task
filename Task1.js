//Write a program in Python or Java that counts backwards from 100 to 1 and prints: 
//“Agile” if the number is divisible by 5, “Software” if the number is divisible by 3, 
//“Testing” if the number is divisible by both, or prints just the number if none of those cases are true.

//The code is written on JavaScript
//To run the code copy files index.htm and Task1.js and run index.htm

let number = 100

for (i=number; i>0; i--) {
    check = 0
    if (i%5===0){
        check+=1
    }
    if (i%3===0){
        check+=2
    }
    if (check===1){
        console.log(i,"Agile")
    } else if (check===2){
        console.log(i,"Software")
    } else if (check===3){
        console.log(i,"Testing")
    } else {
        console.log(i)
    }
}

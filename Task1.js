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
let input=document.getElementById('count')

function decrease(){
    let count=document.getElementById('count').value
    if(count>1){
       input.value=parseInt(count)-1
       console.log(input.value)
    }
}
function increase(l){
    console.log()
    let count=document.getElementById('count').value
   
       input.value=parseInt(count)+1
       

}



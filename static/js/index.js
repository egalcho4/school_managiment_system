const scard=document.querySelectorAll('.scard');
var top_left=document.querySelector('.top-left');
top_left.addEventListener('click',()=>{
    document.getElementById('sidebar').style.width="0px";
    
    top_left.style.display="none";
})
function adduser(){
    var form=document.getElementById('form');
    var user_list=document.getElementById('user_list');
    user_list.style.display="none";
    form.style.display="block";
}
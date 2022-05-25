



   document.addEventListener('DOMContentLoaded', () =>{
    document.querySelector('.menu-toggle').addEventListener('click', function(){
      document.querySelectorAll('.menu-toggle-item').forEach((item,i)=>{
        document.querySelector(
          '.menu-nav').classList.toggle('clicked')
        item.classList.toggle('clicked');
      });
    })
  })

function file_size(elem){
  localStorage.setItem('filesize',elem.files[0].size)
  // document.cookie = `filesize=${elem.files[0].size};max-age=604800`;
}



function LoadNewSearchColoum(){
  var name = document.getElementById("search_index").value 
  if(name.length == 0){
    name = null
  }

  var urls = "/searchs/"+name
  // with Ajax
  // $.ajax({
  //   url: urls,
  //   type: "POST",
  //   dataType: "json",
  //   success: function(datas){
  //     console.log(datas)
  //     $(user_id_column).replaceWith(datas)
  //   }
  // })
  // With dom
  var xhttp;
  xhttp = new XMLHttpRequest();
  xhttp.open("GET", urls, true);

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      const myObj = JSON.parse(this.responseText);
      console.log(myObj)
      document.getElementById("user_id_column").innerHTML = myObj
    
    }
  };

  
  xhttp.send();
}







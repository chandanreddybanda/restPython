const addName = async (event) => {
    var id = document.getElementById("_id").value;
    var name = document.getElementById("name").value;
    var myBody = {'_id':id,'name':name}
    const response = await fetch('http://192.168.29.72:5000/addName', {
      method: 'POST',
      body: JSON.stringify(myBody), // string or object
      headers: {
        'Content-Type': 'text/plain'
      }
    }).then(response => {
        if(response.ok){
            return response.json();
        }
    }).then(text => {
        window.location.href ='home.html';
        window.onload = function() {
            console.log(text);
            document.getElementById("log").innerHTML = text.n;
        }
    });
}
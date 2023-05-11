function login(){
    var Email,password;
        Email = document.getElementById("Email").value
        password =  document.getElementById("Password").value
        

        if(Email  == "prueba@duocuc.cl" && password== "1234"){

            alert("INICIASTE SESION!")

        }   else {
            alert("DATOS INCORRECTOS:(")

        }


}
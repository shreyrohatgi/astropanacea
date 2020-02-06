// addd a subscriber

/* form validation methods */

function subscribe(){

    // Validate Name
    let nameElementId ="name";
    let nameElement = document.getElementById(nameElementId)
    let nameElementTextArea = document.getElementById(nameElementId+'-validation');
    let name = nameElement.value
    console.log("name validation",nameValidationBool(name));
    let validName = false;

    if ( ! nameValidationBool(name)){
        nameElementTextArea.innerHTML = "Name Cannot be empty ! ";
        nameElementTextArea.style.display = 'block';
        console.log("Invalid Name !!")
        }
    else{
        nameElementTextArea.style.display = 'null';
        validName =true ;

    }

    // Validate Email Id
    let emailElementId  = "email";
    let emailElement = document.getElementById(emailElementId);
    let emailElementTextArea = document.getElementById(emailElementId+'-validation');
    let emailId = emailElement.value
    //console.log("value found",value);
    console.log("email validation",emailValidationBool(emailId));
    let validEmail =false;

    if ( ! emailValidationBool(emailId)){
        emailElementTextArea.innerHTML = "Email Id is Invalid ! ";
        emailElementTextArea.style.display = 'block';
        console.log("Invalid Email !!")
        console.log(emailElementTextArea.style.display );

        }
    else{
        emailElementTextArea.style.display = 'null';
        validEmail =true ;

    }


    if (validEmail && validName ){

        // create an ajax request here
        let data = {
                     emailId :emailId,
                     name : name,
                     }

        let url ='/addSubscriber/'

        // turn the subscribe button red //

        let btn =document.getElementById("subscribeButton")
        btn.style.backgroundColor ="red"
        btn.innerHTML = " Subscribed !"
        emailElementTextArea.style.display = 'null';
        nameElementTextArea.style.display = 'null';
        emailElementTextArea.innerHTML ="";
        nameElementTextArea.innerHTML ="";
        console.log("emailElementTextArea");
        console.log(emailElementTextArea.style.display);

        console.log("nameElementTextArea");
        console.log(nameElementTextArea.style.display);

        xhr = makeAjaxPostCall(url,data);






    }

}




function emailValidationBool(emailId){
    /* returns true if email is valid */
    if (emailId.indexOf("@") !== -1){
        return true;
    }else{

        return false;

    }


}

function nameValidationBool(name){
    /* returns true if name is valid */
    if (name.length > 0){
        return true;
    }
    else{
        return false;
    }
}

/* form validation methods */

function submitContactUsForm(){

    // Validate Name
    let nameElementId ="InputName";
    let nameElement = document.getElementById(nameElementId)
    let nameElementTextArea = document.getElementById(nameElementId+'-validation');
    let name = nameElement.value
    console.log("name validation",nameValidationBool(name));
    let validName = false;

    if ( ! nameValidationBool(name)){
        nameElementTextArea.innerHTML = "Name Cannot be empty ! ";
        nameElementTextArea.style.display = 'block';
        console.log("Invalid Name !!")
        }
    else{
        nameElementTextArea.style.display = 'null';
        validName =true ;

    }

    // Validate Email Id
    let emailElementId  = "InputEmail1";
    let emailElement = document.getElementById(emailElementId);
    let emailElementTextArea = document.getElementById(emailElementId+'-validation');
    let emailId = emailElement.value
    //console.log("value found",value);
    console.log("email validation",emailValidationBool(emailId));
    let validEmail =false;

    if ( ! emailValidationBool(emailId)){
        emailElementTextArea.innerHTML = "Email Id is Invalid ! ";
        emailElementTextArea.style.display = 'block';
        console.log("Invalid Email !!")
        console.log(emailElementTextArea.style.display );

        }
    else{
        emailElementTextArea.style.display = 'null';
        validEmail =true ;

    }

    // Extract query
    let queryElementid ="Textarea";
    let queryElement = document.getElementById(queryElementid);
    let query = queryElement.value

    if (validEmail && validName ){

        // create an ajax request here
        let data = {
                     emailId :emailId,
                     name : name,
                     query : query
                     }

        let url ='/addUserQuery/'
        xhr=makeAjaxPostCall(url,data);

        let btn =document.getElementById("contactUsSubmit")
        btn.style.backgroundColor ="red"
        btn.innerHTML = "Submitted !"



    }



}



function makeAjaxPostCall(url,data){

    data = JSON.stringify(data);
    let xhr = new XMLHttpRequest();
    xhr.responseType = "json";
    xhr.onreadystatechange = () => {

        if (xhr.readyState === XMLHttpRequest.DONE){

            return xhr
        }


    }
    xhr.open("POST",url);
    xhr.send(data);


}

/*
var txt = "";
if ('files' in x) {
    if (x.files.length == 0) {
        txt = "Select one or more files.";
    } else {
        for (var i = 0; i < x.files.length; i++) {
            txt += "<br><strong>" + (i+1) + ". file</strong><br>";
            var file = x.files[i];
            if ('name' in file) {
                txt += "name: " + file.name + "<br>";
            }
            if ('size' in file) {
                txt += "size: " + file.size + " bytes <br>";
            }
        }
    }
}
document.getElementById ("demo").innerHTML = txt;
*/
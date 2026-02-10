let name=prompt("Who are you", "");

if(name==="admin")
{
    let pass=prompt("Enter a password", "");
    if (pass==="abuka2006")
        alert("Welcome");

    else if (pass==="" || pass===null )
        alert("Canceled");
    else 
        alert("Wrong password");
}
else if (userName === '' || userName === null) {
  alert( 'Canceled' );
} else {
  alert( "I don't know you" );
}
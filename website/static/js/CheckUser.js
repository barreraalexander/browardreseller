function checkUser (){
    let user_id = localStorage.getItem('user_id');
    if (user_id != NaN){
        // alert(user_id);
        let new_id = 'getRandom'
        localStorage.setItem('user_id', new_id)
        return new_id;
    } else {
        return user_id;
    }
}


function displayID (){
    let user_id = checkUser();
    let id_p = document.querySelector('#temp_id');
    id_p.innerHTML = user_id;
    // let test = document.getElementById('temp_id')
    
    alert('ram');
}

// displayID();
function checkUser(){let user_id=localStorage.getItem('user_id');if(user_id!=NaN){let new_id='getRandom'
localStorage.setItem('user_id',new_id)
return new_id;}else{return user_id;}}
function displayID(){let user_id=checkUser();let id_p=document.querySelector('#temp_id');id_p.innerHTML=user_id;alert('ram');}
function submitRemove(model_id){let remove_input=document.querySelector('#removing_id')
remove_input.setAttribute('value',model_id);let submit_btn=document.querySelector('#submit_remove');submit_btn.click();}
var open_ann=false;var exp_sect=document.querySelector('#index_section1');var slider_ctnr=exp_sect.querySelector('#ann_slider_ctnr');var max_btn=exp_sect.querySelector('#maxim_svg_ctnr');var min_btn=exp_sect.querySelector('#minim_svg_ctnr');console.log(slider_ctnr);function modAnnouncements(){console.log('run');if(open_ann==false){exp_sect.style.height='15em';exp_sect.style.padding='1em';slider_ctnr.classList.toggle('invisible');min_btn.classList.toggle('invisible');max_btn.classList.toggle('invisible');open_ann=true;}else if(open_ann==true){exp_sect.style.height='initial'
exp_sect.style.padding='initial';slider_ctnr.classList.toggle('invisible');max_btn.classList.toggle('invisible');min_btn.classList.toggle('invisible');open_ann=false;}}
exp_sect.addEventListener('click',modAnnouncements);function redir(url){window.location.href=url;};
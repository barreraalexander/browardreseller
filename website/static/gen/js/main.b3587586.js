var open_ann=false;var exp_btn=document.querySelector('#maxim_svg_ctnr');var exp_sect=document.querySelector('#index_section1')
function modAnnouncements(){console.log('run');if(open_ann==false){exp_sect.style.height='15em';}}
exp_btn.addEventListener('click',modAnnouncements);
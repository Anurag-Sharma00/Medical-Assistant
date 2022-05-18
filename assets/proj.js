$(document).ready(function(){
$.getJSON('/specializationdisplayallJSON',function(data){

    data.result.map((item)=>{
    $('#q').append($('<option>').text(item.specialization).val(item.question))

    })

})


})
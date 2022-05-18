var i=0
var ques=[]
var result=[]

// Sub-Questions
function subquestion()
{
  var qnum=1

  subques=ques[i].subquestions.split('#')
  var shtm=""
  var blockname=['Normal','Mild','Modrate','Severe','Extreme']
  for(j=0;j<subques.length;j++){
    shtm+=`<div class='col s12' style="margin-top: 10px;margin-bottom:5px;font-size:12px;font-weight:600">Q${(j+1)}: ${subques[j]}</div>`
    for(block=0;block<5;block++){
    shtm+=`<div value='${block+1}' class="col blocks block-color"  style="margin-left:8px;width:65px;height:58px;font-weight: 500;" id="rate${qnum}${block}">${blockname[block]}<br>${block+1}</div>`
    }
    qnum+=1
  }
  $('#subquestiondiv').html(shtm)

  $('#heading').html($('#splname').val()+' '+'index'+' '+(i+1)+'/'+ques.length)
}

$(document).ready(function(){

$.getJSON('/userquestion',{splid:$('#spl').val()},function(data){
//alert(JSON.stringify(data))

  ques=data.result
  htm="Q"+ques[i].questionnumber+": "+ques[i].question
  $('#questiondiv').html(htm)

  subquestion()
})

$('#btnnext').click(function(){
  i++
  if(i<ques.length){
  htm="Q"+ques[i].questionnumber+":"+ques[i].question
  $('#questiondiv').html(htm)
  subquestion()
   }


// Previous Button Manupilation
  if(ques.length>=1){
           $('#btnnext1').removeClass('col s12').addClass('col s6')
           $('#btnprev').addClass('col s6')
           temp1=`<button id="btnprev1" style="width:100%;border-radius:20px;background:rgb(17, 194, 214);" class=" waves-effect wave-light btn" type="button" name="action">Preivous</button>`
           $('#btnprev').html(temp1)
        }

  $('#btnprev1').click(function(){
  i--
  if(i<ques.length){
  htm="Q"+ques[i].questionnumber+":"+ques[i].question
  $('#questiondiv').html(htm)
  subquestion()
   }

 if(i==0){
    $('#btnprev').html('')
    $('#btnprev').removeClass('col s6')
    $('#btnnext1').removeClass('col s6').addClass('col s12')
  }
  })

})





function onclicks(blockid){

    temp=blockid.slice(0,blockid.length-1)
    alert(temp)
    for(k=0;k<5;k++){
        $("#"+temp+String(k)).removeClass('block-onclick-color').addClass('block-color')
    }
    $("#"+blockid).removeClass('block-color').addClass('block-onclick-color')



}


$(document).click(function(event){
        //change div color
        blockid=event.target.id

        //onclock div color change
        onclicks(blockid)


    })




})





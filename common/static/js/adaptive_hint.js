function hide_hint() {
    //initially hide all hints
    var index = arguments[0];
    var hintInputId = hintIds[index];
    var proId = proIds[index];
    var hintId = hintInputId.replace('input', 'problem');
    hintId = hintId.slice(0, -4);
    var hintEle = document.getElementById(hintId)
    if (!hintEle) {
      return;
    }
    var hintInputEle = document.getElementById(hintInputId)
    if (!hintInputEle) {
      return;
    }
    var hintStatusId = hintInputId.replace('input', 'status');
    var hintStatusEle = document.getElementById(hintStatusId);
    if (!hintStatusEle) {
      return;
    }
    hintEle.style.display = "none";
    hintInputEle.value = "";
    hintStatusEle.className = "incorrect";
}

function show_hint() {
  //show "show hint" button after certain minutes
  //pass in hint index and number of minutes to delay
  var hint_number = arguments[0];
  var minutes = 3;//arguments[1];
  var seconds_diff = minutes*60*1000;
  var timer_diff = Date.now() - timerStart;
  if (timer_diff > seconds_diff) {
    for (var i=0; i < hint_number; i++) {
      var hintDivId = hintTextIds[i]+"_hintDiv";
      if (document.getElementById(hintDivId)) {
        document.getElementById(hintDivId).style.display = "";
      }
    }
  }
}


function show_hint_in_problem() {
  //show hint when the "show hint" button is clicked
    var index = arguments[0];
    var hintInputId = hintIds[index];
    var hintId = hintInputId.replace('input', 'problem');
    hintId = hintId.slice(0, -4);
    var hintTextId = hintTextIds[index];
    var hintAnswerId = hintTextId + "answer";
    var hintStatusId = hintInputId.replace('input', 'status');
    var proInputId = proIds[index];
    var proId = proInputId.replace('input', 'status');
    
    var hintInputEle = document.getElementById(hintInputId);
    if (!hintInputEle) {
         return;
    }
    var hintEle = document.getElementById(hintId);
    if (!hintEle) {
         return;
    }
    var hintAnswerEle = document.getElementById(hintAnswerId);
    if (!hintAnswerEle) {
         return;
    }
    var hintStatusEle = document.getElementById(hintStatusId);
    if (!hintInputEle) {
         return;
    }
    var proInputBox = document.getElementById(proInputId);
    if (!proInputBox) {
         return;
    }
    var proEle = document.getElementById(proId);
    if (!proEle) {
         return;
    }
         
    if (proEle.classList.contains("incorrect")) {
      if (proInputBox.value != "") {
        if (document.getElementById(hintTextId)) {
          var hintText = document.getElementById(hintTextId).innerHTML;
          document.getElementById(hintId).style.display = "";
          document.getElementById(hintId).getElementsByTagName('p')[0].innerHTML = hintText;
          document.getElementById(hintStatusId).className = "unanswered";
        }
      }
    }
}

$(function() {
    $('.show_hint_button').click(function () {
        var problem_info = $('.hint').attr('id');
        $.ajax({
            url: '/',
            type: 'post',
            datatype: 'json',
            data: {'name': 'zzhai', 'problem_info': problem_info}
        });
    });
});


function show_textHint_in_problem() {
  // show text hint when "show hint" button is clicked
    var index = arguments[0];
    var hintTextId = hintTextIds[index];
    hintTextId += "_textHint";
    var proEle = document.getElementById(hintTextId);
    proEle.style.display = "";
}


function show_hint_in_hint() {
  // want to make sure the hint is not hidden after student
  // clicks check/save/reset which will reload the js of the hint
    var index = arguments[0];
    index = index - 1;
    var hintInputId = arguments[1];
    hintInputId = hintInputId[index];
    var proId = arguments[2];
    proId = proId[index];
    var hintTextId = arguments[3];
    hintTextId = hintTextId[index];

    var hintAnswerId = hintTextId + "answer";
    var tolerance = 1+Math.exp(-6);
  
    var hintId = hintInputId.replace('input', 'problem');
      hintId = hintId.slice(0, -4);
    
    var proInputBox = document.getElementById(proId);
    proId = proId.replace('input', 'status');
    var prohintId = proId.replace('input', 'inputtype');
    var ele = document.getElementById(proId);
    if (ele.classList.contains("incorrect")) {
      if (proInputBox.value != "") {
        if (document.getElementById(hintTextId)) {
          var hintText = document.getElementById(hintTextId).innerHTML;
          document.getElementById(hintId).style.display = "";
          document.getElementById(hintId).getElementsByTagName('p')[0].innerHTML = hintText;
          var hintStatusId = hintInputId.replace('input', 'status');

          var inputValue = document.getElementById(hintInputId).value;
          inputValue = eval(inputValue);
          var answerValue = document.getElementById(hintAnswerId).innerHTML;
          answerValue = answerValue.substring(1);
          answerValue = answerValue.slice(0,-1);
          answerValue = eval(answerValue);

          if (answerValue == 0) {
            if (inputValue == 0) {
              document.getElementById(hintStatusId).className = "correct";
            } else {
              document.getElementById(hintStatusId).className = "incorrect";
            }
          } else {
            var ratio = inputValue / answerValue;
              if (ratio < tolerance && ratio > (1/tolerance)) {
                  document.getElementById(hintStatusId).className = "correct";
              }
          }
        }
      }
    }
}
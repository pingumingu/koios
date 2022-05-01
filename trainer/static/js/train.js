const problem_list = JSON.parse(document.getElementById('problem_list').textContent);

function toggleDiv(id) {
    var div = document.getElementById("problem_instance_"+id);
    div.style.visibility = div.style.visibility == "hidden" ? "visible" : "hidden";
}

function timeDelta(times) {
  return (times.map((element, index, array) => element - (array[index - 1] ?? 0)).slice(1))
}

function cycleVisibility(times) {
    //ev.preventDefault();
  
    // get a nodeList of all the divs
    const nlist = document.querySelectorAll('div.cycle-hide');
  
    for (let i = 0; i < nlist.length; i++) {
  
      // if div is active, that class name will be removed
      if (nlist[i].className.includes('active')) {
        nlist[i].classList.remove('active');
  
        // check wheter you're at the end of nodeList 
        const nextIndex = i < nlist.length - 1 ? i + 1 : 0;
        
        if (nextIndex == 0) {
          // converts milliseconds to seconds
          time_taken = timeDelta(times).map((element) => Math.round(element/1000));
          var j = 0;
          problem_list.forEach( problem => {
            document.getElementById("time_taken_"+problem.id).innerHTML = "Time taken: " +String(time_taken[j]) +" seconds";
            j = j+1;
          });
          var results_page = document.getElementById("results-page");
          results_page.removeAttribute('id');
          results_page.classList.add('active');
        } else {
          // and add the class that makes next div visible
          nlist[nextIndex].classList.add('active');
          // focuses the next div input box
          nlist[nextIndex].querySelector("input").focus();
        }

  
        // exit the loop
        break;
      }
    }
  }



//code for verifying if a solution is correct or not
window.onload = function() {
    var start = Date.now()
    var times = [start]
    //first div.cycle-hide element is shown
    document.querySelector('div.cycle-hide').classList.add('active');
    // for each problem in problem_list passed through the context, add event listeners for the input box to test answer validity
    problem_list.forEach( problem => {
        answer_box = document.getElementById(problem.id+"_input")
        answer_box.addEventListener("input", function(event) {
            //console.log(event.target.value)
            if (event.target.value == problem.solution) {
                event.target.value = "";
                times.push(Date.now());
                cycleVisibility(times);
            };  
          });
    })
}

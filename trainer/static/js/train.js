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
          time_taken = timeDelta(times);
          var j = 0;
          problem_list.forEach( problem => {
            document.getElementById("time_taken_"+problem.id).innerHTML = String(time_taken[j]);
            console.log(document.getElementById("time_taken_"+problem.id))
            j = j+1;
          });
          console.log(j);
          var results_page = document.getElementById("results-page");
          results_page.removeAttribute('id');
          results_page.classList.add('active');
        } else {
          // and add the class that makes next div visible
          nlist[nextIndex].classList.add('active');
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
        document.getElementById(problem.id+"_input").addEventListener("input", function(event) {
            //console.log(event.target.value)
            if (event.target.value == problem.solution) {
                event.target.value = "";
                times.push(Date.now());
                cycleVisibility(times);
            };  
          });
    })
}

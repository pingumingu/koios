const problem_list = JSON.parse(document.getElementById('problem_list').textContent);

function toggleDiv(id) {
    var div = document.getElementById("problem_instance_"+id);
    div.style.visibility = div.style.visibility == "hidden" ? "visible" : "hidden";
}
window.onload = function() {
    problem_list.forEach( problem => {
        console.log(problem.id+"_input");
        document.getElementById(problem.id+"_input").addEventListener("input", function(event) {
            console.log(event.target.value)
            if (event.target.value == problem.solution) {
                document.getElementById("problem_instance_"+problem.id).style.color = "green"
            }   else {
                document.getElementById("problem_instance_"+problem.id).style.color = "black"       
            };  
          });
    })
}

function toggleDiv(id) {
    var div = document.getElementById("problem_instance_"+id);
    div.style.visibility = div.style.visibility == "hidden" ? "visible" : "hidden";
}
const needle = document.querySelector(".needle");

function to_z1(){
  needle.style.transform = "translate(-50%, -50%) rotate(-100deg)";
}

function to_z2() {
  needle.style.transform = "translate(-50%, -50%) rotate(-50deg)";
}

function to_z3() {
  needle.style.transform = "translate(-50%, -50%) rotate(0deg)";
}

function to_z4() {
  needle.style.transform = "translate(-50%, -50%) rotate(50deg)";
}

function to_z5() {
  needle.style.transform = "translate(-50%, -50%) rotate(100deg)";
}

if (targetValue === "1") {
  to_z1();
} else if (targetValue === "2") {
  to_z2();
} else if (targetValue === "3") {
  to_z3();
} else if (targetValue === "4") {
  to_z4();
} else {
  to_z5();
}
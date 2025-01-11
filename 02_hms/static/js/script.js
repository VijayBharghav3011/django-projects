var a = document.getElementById('togglePassword');
var p = document.getElementById('password');
console.log(p);

a.addEventListener('click', function (e) {
   const type = p.getAttribute('type') === 'password' ? 'text' : 'password';
   p.setAttribute('type', type);
   this.classList.toggle('fa-eye-slash');
});



function myFunction() {
   document.getElementById("myDropdown").classList.toggle("show");
 }

window.onclick = function(event) {
   if (!event.target.matches('.profile_btn')) {
       var dropdowns = document.getElementById("myDropdown");
       var i;
       for (i = 0; i < dropdowns.length; i++) {
           var openDropdown = dropdowns[i];
           if (openDropdown.classList.contains('show')) {
               openDropdown.classList.remove('show');
           }
       }
   }
}


function searchFilter() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (var i = 1; i < tr.length; i++) {
      var tds = tr[i].getElementsByTagName("td");
      var flag = false;
      for(var j = 0; j < tds.length; j++){
        var td = tds[j];
        if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
          flag = true;
        }
      }
      if(flag){
          tr[i].style.display = "";
      }
      else {
          tr[i].style.display = "none";
      }
    }
  }


let email = document.querySelector('#mail');
let error = document.querySelector('#errors');

email.addEventListener('input', function(e) {
    let val = e.target.value;
    console.log(val);
    const emailRegex = /^\w+([\.-]?\w+)*(\@\w{5,10})+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (emailRegex.test(val)) {
        error.textContent ="";
    }
    else {
        error.textContent = "Please Enter Valid Email";
    }
});



let ab = document.querySelector('#phonenumber');
let bc = document.querySelector('#err');

ab.addEventListener('input', function(e) {
    let c = e.target.value;
    console.log(c);
    const verify = /^\+?[1-9]\d{11,13}$/;
    if (verify.test(c)) {
        bc.textContent ="";
    }
    else {
        bc.textContent = "Please Enter Valid Phone Number ex: +91914*******";
    }
});

// function formValidation() {
//     var firstname =  document.getElementById('firstname');
//     var lastname = document.getElementById('lastname');
//     var education = document.getElementById('education');
//     var designation = document.getElementById('designation');
//     var language_known = document.getElementById('language_known');

//     var check_file = document.getElementById('img');
//     var check_dob = document.getElementById('dob');
//     var check_join_date = document.getElementById('joining_date');
//     var check_phone = document.getElementById('phonenumber');

//     if (!validateFN(firstname)) {
//         return false;
//     }

//     if (!validateLN(lastname)) {
//         return false;
//     }

//     if (!validateEdu(education)) {
//         return false;
//     }

//     if (!validateDes(designation)) {
//         return false;
//     }

//     if (!validateEdu(language_known)) {
//         return false;
//     }

//     if (!validateImage(check_file)) {
//         return false;
//     }

//     if (!validateDate(check_dob)) {
//         return false;
//     }
//     if (!validateJoinDate(check_join_date)) {
//         return false;
//     }

//     if (!validatePhoneNumber(check_phone)) {
//         return false;
//     }

//     return true;
// }

// function validateFN(fn) {
//     var fn_val = fn.value;
//     var allowed_name = /^[a-zA-Z]+(?: [a-zA-z]+)*$/;
//     if (!allowed_name.test(fn_val)){
//         alert('First Name should contain only letter and space');
//         fn.value = '';
//         return false;
//     }
//     return true;
// }

// function validateLN(fn) {
//     var ln_val = fn.value;
//     var allowed_name = /^[a-zA-Z]+(?: [a-zA-z]+)*$/;
//     if (!allowed_name.test(ln_val)){
//         alert('Last Name should contain only letter and space');
//         fn.value = '';
//         return false;
//     }
//     return true;
// }

// function validateEdu(edu) {
//     var edu_val = edu.value;
//     var allowed_name = /^[a-zA-Z,]+(?: [a-zA-z,]+)*$/;
//     if (!allowed_name.test(edu_val)){
//         alert('Eduaction should contain only letter and space');
//         fn.value = '';
//         return false;
//     }
//     return true;
// }

// function validateDes(Des) {
//     var Des_val = fn.value;
//     var allowed_name = /^[a-zA-Z]+(?: [a-zA-z]+)*$/;
//     if (!allowed_name.test(Des_val)){
//         alert('Designation should contain only letter and space');
//         fn.value = '';
//         return false;
//     }
//     return true;
// }

// function validateEdu(language_known) {
//     var edu_val = edu.value;
//     var allowed_name = /^[a-zA-Z,]+(?: [a-zA-z,]+)*$/;
//     if (!allowed_name.test(edu_val)){
//         alert('Language should contain only letter and space');
//         fn.value = '';
//         return false;
//     }
//     return true;
// }

// function validateImage(fileInput) {
//     var filePath = fileInput.value;
//     var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;

//     if (!allowedExtensions.exec(filePath)) {
//         alert('Invalid file type. Please upload an image file (jpg, jpeg, png, gif).');
//         fileInput.value = '';
//         return false;
//     }

//     var fileSize = fileInput.files[0].size;
//     var maxSize = 1024 * 1024; // 1MB
//     if (fileSize > maxSize) {
//         alert('File size exceeds 1MB. Please upload a smaller image.');
//         fileInput.value = '';
//         return false;
//     }

//     return true;
// }

// function validateDate(dateInput) {
//     var inputDate = new Date(dateInput.value);
//     var currentDate = new Date();

//     if (inputDate >= currentDate) {
//         alert('Date must be in the past.');
//         dateInput.value = '';
//         return false;
//     }

//     return true;
// }

// function validateJoinDate(dateInput) {
//     var inputDate = new Date(dateInput.value);
//     var currentDate = new Date();

//     if (inputDate >= currentDate) {
//         alert('Date must be in the past.');
//         dateInput.value = '';
//         return false;
//     }

//     return true;
// }

// function validatePhoneNumber(phoneInput) {
//     var phoneNumber = phoneInput.value;

//     var phonePattern =/^\+?[1-9]\d{11,13}$/;

//     if (!phonePattern.test(phoneNumber)) {
//         alert('Invalid phone number format. Please enter a 10-digit number.');
//         phoneInput.value = '';
//         return false;
//     }

//     return true;
// }


function formValidation() {
    var firstname = document.getElementById('firstname');
    var lastname = document.getElementById('lastname');
    var education = document.getElementById('education');
    var designation = document.getElementById('designation');
    var language_known = document.getElementById('language_known');
    var check_file = document.getElementById('img');
    var check_dob = document.getElementById('dob');
    var check_join_date = document.getElementById('joining_date');
    var check_phone = document.getElementById('phonenumber');

    if (!validateFN(firstname)) {
        return false;
    }

    if (!validateLN(lastname)) {
        return false;
    }

    if (!validateEdu(education)) {
        return false;
    }

    if (!validateDes(designation)) {
        return false;
    }

    if (!validateLang(language_known)) {
        return false;
    }

    if (!validateImage(check_file)) {
        return false;
    }

    if (!validateDate(check_dob)) {
        return false;
    }

    if (!validateDate(check_join_date)) {
        return false;
    }

    if (!validatePhoneNumber(check_phone)) {
        return false;
    }

    return true;
}

function validateFN(fn) {
    var fn_val = fn.value.trim();
    var allowed_name = /^[a-zA-Z]+(?: [a-zA-Z]+)*$/;
    if (!allowed_name.test(fn_val)){
        alert('First Name should contain only letters and spaces');
        fn.value = '';
        return false;
    }
    return true;
}

function validateLN(ln) {
    var ln_val = ln.value.trim();
    var allowed_name = /^[a-zA-Z]+(?: [a-zA-Z]+)*$/;
    if (!allowed_name.test(ln_val)){
        alert('Last Name should contain only letters and spaces');
        ln.value = '';
        return false;
    }
    return true;
}

function validateEdu(edu) {
    var edu_val = edu.value.trim();
    var allowed_edu = /^[a-zA-Z,]+(?: [a-zA-Z,]+)*$/;
    if (!allowed_edu.test(edu_val)){
        alert('Education should contain only letters, commas, and spaces');
        edu.value = '';
        return false;
    }
    return true;
}

function validateDes(des) {
    var des_val = des.value.trim();
    var allowed_des = /^[a-zA-Z]+(?: [a-zA-Z]+)*$/;
    if (!allowed_des.test(des_val)){
        alert('Designation should contain only letters and spaces');
        des.value = '';
        return false;
    }
    return true;
}

function validateLang(lang) {
    var lang_val = lang.value.trim();
    var allowed_lang = /^[a-zA-Z,]+(?: [a-zA-Z,]+)*$/;
    if (!allowed_lang.test(lang_val)){
        alert('Known Language should contain only letters, commas, and spaces');
        lang.value = '';
        return false;
    }
    return true;
}

function validateImage(fileInput) {
    var filePath = fileInput.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    var maxSize = 1024 * 1024; // 1MB

    if (!allowedExtensions.test(filePath)) {
        alert('Invalid file type. Please upload an image file (jpg, jpeg, png, gif).');
        fileInput.value = '';
        return false;
    }

    if (fileInput.files[0].size > maxSize) {
        alert('File size exceeds 1MB. Please upload a smaller image.');
        fileInput.value = '';
        return false;
    }

    return true;
}

function validateDate(dateInput) {
    var inputDate = new Date(dateInput.value);
    var currentDate = new Date();

    if (inputDate >= currentDate) {
        alert('Date must be in the past.');
        dateInput.value = '';
        return false;
    }

    return true;
}

function validatePhoneNumber(phoneInput) {
    var phoneNumber = phoneInput.value.trim();
    var phonePattern =/^\+?[1-9]\d{11,13}$/;

    if (!phonePattern.test(phoneNumber)) {
        alert('Invalid phone number format. Please enter a 10-digit number.');
        phoneInput.value = '';
        return false;
    }

    return true;
}

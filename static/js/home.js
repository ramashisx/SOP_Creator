const button = document.getElementById("btn-predict");
const result = document.getElementById("result");
result.innerText = "result here";


button.addEventListener( "click", ev =>  {

    const form_data = new FormData();

    const name = document.getElementById("name");
    const college = document.getElementById("college");
    const course = document.getElementById("course");
    const country = document.getElementById("country");
    const family = document.getElementById("family");
    const ielts = document.getElementById("ielts");
    const academics = document.getElementById("academics");
    const experience = document.getElementById("experience");
    const gic = document.getElementById("gic");
    const fees = document.getElementById("fees");

    form_data.append("name", name.value)
    form_data.append("college", college.value)
    form_data.append("course", course.value)
    form_data.append("country", country.value)
    form_data.append("family", family.value)
    form_data.append("ielts", ielts.value)
    form_data.append("academics", academics.value)
    form_data.append("experience", experience.value)
    form_data.append("gic", gic.value)
    form_data.append("fees", fees.value)

    for (const pair of form_data.entries()) {
    console.log(pair[0]+ ', ' + pair[1]);
    }

    $.ajax({
        type: 'POST',
        url: '/bot',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        async: true,
        success: function (data) {
            result.innerText = "done";
            console.log('Success!');
        },
    });

});
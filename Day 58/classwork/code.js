// const -მა შექმნა საცავი რომელსაც დავარქვი სახელი და მივეცი ინფორმაცია //
const gmiri = {
    name: "ვინც არი",
    age: "ჩემზე უფროსია 100%",
    height: "მაღალი 100%",
    weight: "მერავი რა გინდა ავწონო",
    also: "აღარ ვიცი რა დავწერო იმედია ეს გამოდგება"
}

// აქ ცა; ცალკე გამოვიძახე მონაცემები //
console.log(gmiri)
console.log(gmiri.name)
console.log(gmiri.age)
console.log(gmiri.height)
console.log(gmiri.weight)
console.log(gmiri.also)

gmiri.name = "ანუ სახელი ხო ექნება და თუ არ აქვს მოუგონე რას მიყურებ"

// არ ვაპირებ ავხსნა რატომ ამოვშალე //
delete gmiri.weight;

console.log(gmiri.name)
console.log(gmiri.age)
console.log(gmiri.height)
console.log(gmiri.also)
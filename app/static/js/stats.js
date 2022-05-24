let stats = document.getElementsByClassName('subtitle')
let currStreak = stats[0]
let bestStreak = stats[1]
let guessesDist = stats[2]

let authtoken
let userStats

$.ajax('/api/getuserstats', {
    type: 'POST',
    async: false,
    data: JSON.stringify({authtoken : authtoken}),
    contentType: 'application/json',
    dataType: 'json',
    success: function(data) {
      userStats = data
    }
  })

currStreak.innerHTML = "Current Streak: " + userStats[currStreak]
bestStreak.innerHTML = "Best Streak: " + userStats[currStreak]
guessesDist.innerHTML = "Guess Breakdown: " + userStats[currStreak]

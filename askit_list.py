from askit.models import *

all_posts = Post.objects.all()
question_update = [{
  "question": "What is the smallest thing for which you are grateful?",
  "body": "Technology while using the toilet.",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 2,
  "cookie_count": 3,
  # "created_at": "5 months, 1 day, 16 hours",
  # "updated_at": "5 months, 1 day, 16 hours",
}, {
  "question": "Who has had the most positive impact on your life?",
  "body": "Rocky Balboa",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 2,
  "cookie_count": 2,
  # "created_at": "5 months, 1 day, 12 hours",
  # "updated_at": "5 months, 1 day, 12 hours",
}, {
  "question": "If you could use a time machine, would you rather have one that only goes back in time or only goes forward?",
  "body": "Back in time! I would never die!",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 3,
  "cookie_count": 3,
  # "created_at": "4 months, 25 days, 2 hours",
  # "updated_at": "4 months, 25 days, 2 hours",
}, {
  "question": "Let's say you got a promotion, a job, a college acceptance, an accolade/award, or just generally accomplished something major.",
  "body": "Who is the first person you'd tell and how do you think they'd react?",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 0,
  "cookie_count": 1,
  # "created_at": "4 months, 25 days, 2 hours",
  # "updated_at": "4 months, 25 days, 2 hours",
}, {
  "question": "Is Die Hard a Christmas movie?",
  "body": "It is. There's no argument.",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 8,
  "cookie_count": 8,
  # "created_at": "4 months, 25 days, 2 hours",
  # "updated_at": "4 months, 25 days, 2 hours",
}, {
  "question": "Would you rather be caught telling a lie, or have people not believe you when you tell the truth?",
  "body": "This is tough.. I definitely think I would rather not have people believe me when I tell the truth…",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 2,
  "cookie_count": 3,
  # "created_at": "4 months, 20 days, 30 minutes",
  # "updated_at": "4 months, 20 days, 30 minutes",
}, {
  "question": "If you were an inanimate object, what would you be and why?",
  "body": "A Red Ryder, carbine action, two-hundred shot range model air rifle!",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 3,
  "cookie_count": 2,
  # "created_at": "4 months, 20 days, 30 minutes",
  # "updated_at": "4 months, 20 days, 30 minutes",
}, {
  "question": "If you could be good at any profession without having to receive the accompanying education or trade experience, which would you choose?",
  "body": "Game show host.",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 12,
  "cookie_count": 9,
  # "created_at": "4 months, 20 days, 30 minutes",
  # "updated_at": "4 months, 20 days, 30 minutes",
}, {
  "question": "What is something you're terrible at but wish you could do well?",
  "body": "Remembering birthdays..",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 11,
  "cookie_count": 3,
  # "created_at": "4 months, 10 days, 3 hours",
  # "updated_at": "4 months, 10 days, 3 hours",
}, {
  "question": "What is the quality you admire the most in the person you dislike the most?",
  "body": "Ambition (Hitler?)",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 2,
  "cookie_count": 8,
  # "created_at": "4 months, 10 days, 3 hours",
  # "updated_at": "4 months, 10 days, 3 hours",
}, {
  "question": "What are the books/movies/games that never get old and always make you feel better when you get down?",
  "body": "Calvin & Hobbes, Top Gun, Playstation 2 games.",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 4,
  "cookie_count": 1,
  # "created_at": "3 months, 28 days, 20 hours",
  # "updated_at": "3 months, 28 days, 20 hours",
}, {
  "question": "How much sawdust can you put into a Rice Krispie Treat before people start to notice?",
  "body": "Depends who's watching, but probably a few ounces.",
  "author": "nolan_dugger@gmail.com",
  "upvote_count": 1,
  "cookie_count": 4,
  # "created_at": "3 months, 28 days, 20 hours",
  # "updated_at": "3 months, 28 days, 20 hours",
}, {
  "question": "On an average day, how many pigeons do you think you could reasonably carry?",
  "body": "10, if they all stood horizontally on my arm.",
  "author": "Cookietest@yahoo.com",
  "upvote_count": 0,
  "cookie_count": 1,
  # "created_at": "3 months, 28 days, 20 hours",
  # "updated_at": "3 months, 28 days, 20 hours",
}, {
  "question": "What are you proud of, but never have an excuse to talk about",
  "body": "Becoming a sponsored World of Warcraft player!",
  "author":"Cookietest@yahoo.com",
  "upvote_count": 1,
  "cookie_count": 3,
  # "created_at": "3 months, 28 days, 19 hours",
  # "updated_at": "3 months, 28 days, 19 hours",
}, {
  "question": "If all animals were the same size, what would win in a fight?" ,
  "body": "Rainbow shrimp!",
  "author":"Cookietest@yahoo.com",
  "upvote_count": 4,
  "cookie_count": 1,
  # "created_at": "3 months, 1 day, 16 hours",
  # "updated_at": "3 months, 28 day, 16 hours",
}, {
  "question": "How many 2nd Graders could YOU beat up if they came at you in waves of 10, with a 5th Grader boss every 5 rounds? What would your strategy be?",
  "body": "I think I could take at least 10 waves. I would find a confined space where I could funnel them in one at a time, and I would use my legs/reach advantage!",
  "author": "askit_test7@gmail.com",
  "upvote_count": 6,
  "cookie_count": 3,
  # "created_at": "3 months, 28 day, 16 hours",
  # "updated_at": "3 months, 28 day, 16 hours",
}, {
  "question": "You come across an old lady and baby drowning in a pool. You can only save one. Who do you save and why?",
  "body": "Depends on the old lady and the baby.... Probably the baby more often than not, because I'm a good person.",
  "author": "askit_test7@gmail.com",
  "upvote_count": 9,
  "cookie_count": 10,
  # "created_at": "3 months, 28 day, 15 hours",
  # "updated_at": "3 months, 28 day, 15 hours",
}, {
  "question": "What's one superpower you WOULDN'T want?",
  "body": "Laser eyes. One sneeze, something precious is gone.",
  "author": "askit_test7@gmail.com",
  "upvote_count": 1,
  "cookie_count": 5,
  # "created_at": "3 months, 28 day, 14 hours",
  # "updated_at": "3 months, 28 day, 14 hours",
}, {
  "question": "Favorite color, birthday, name of their first pet, and Mother's maiden name.",
  "body": "No reason..",
  "author": "askit_test7@gmail.com",
  "upvote_count": 5,
  "cookie_count": 3,
  # "created_at": "3 months, 12 day, 1 hour",
  # "updated_at": "3 months, 12 day, 1 hour",
}, {
  "question": "Is a hot dog considered a sandwich?",
  "body": "Discuss!",
  "author": "askit_test7@gmail.com",
  "upvote_count": 2,
  "cookie_count": 1,
  # "created_at": "3 months, 12 day, 1 hour",
  # "updated_at": "3 months, 12 day, 1 hour",
}]


for i in range(len(question_update)-1):
    posts = all_posts[i]
    posts.question = question_update[i]['question']
    posts.body = question_update[i]['body']
    posts.upvote_count = question_update[i]['upvote_count']
    posts.cookie_count = question_update[i]['cookie_count']
    user = User.objects.get(username=question_update[i]['author'])
    posts.author = user
    posts.save()
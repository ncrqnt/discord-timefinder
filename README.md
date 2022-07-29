# DiscordTimeFinder

Discord Bot for voting on a suitable time (e.g. for movie nights, game sessions, etc.).

## Plan

### Phase 1 - Basic functions

- [x] Working slash command: `/findtime`
- [x] Parameters
  - [x] `earliest`: earliest time for finding time **in UTC** (12h OR 24h format, e.g. 11:00pm / 23:00)
  - [x] `latest`: latest time for finding time **in UTC**
  - [x] `interval`: interval of suggested times (e.g. quarter, half or full hours)
- [x] Generate time spans
  - [x] Cut on 24 reactions / time suggestions
  - [x] React with alphabetical emojis for voting

### Phase 2 - Comfort
- [ ] Paramters
  - [ ] `date`: Date of the event (format: `YYYY-MM-dd`)
  - [ ] `timezone`: Pre-defined timezones to convert from
- [ ] Close voting via button/command
  - [ ] If possible: only creator + admins can close
  - [ ] Count votes (-1 for to exclude bots vote)
  - [ ] Remove old post and post top 3 times

### Future ideas
- [ ] Define period for how long vote is open, close automatically afterwards
# DiscordTimeFinder

Discord Bot for voting on a suitable time (e.g. for movie nights, game sessions, etc.).

## Plan

### Phase 1 - Basic functions

- [ ] Working slash command: `/findtime`
- [ ] Parameters
  - [ ] `earliest`: earliest time for finding time **in UTC** (12h OR 24h format, e.g. 11:00pm / 23:00)
  - [ ] `latest`: latest time for finding time **in UTC**
  - [ ] `date`: Date of the event (format: `YYYY-MM-dd`)
  - [ ] (interval hourly)
- [ ] Generate time spans
  - [ ] Cut on 24 reactions / time suggestions
  - [ ] React with A - X

### Phase 2 - Comfort
- [ ] Paramters
  - [ ] `interval`: interval of suggested times (e.g. quarter, half or full hours)
- [ ] Close voting via button/command
  - [ ] If possible: only creator + admins can close
  - [ ] Count votes (-1 for to exclude bots vote)
  - [ ] Remove old post and post top 3 times

### Future ideas
- [ ] Define period for how long vote is open, close automatically afterwards
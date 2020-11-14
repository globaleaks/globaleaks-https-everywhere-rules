# HTTPS-Everywhere Rulesets for GlobaLeaks

## Updating the directory

### Adding a new organization

1. Ensure to collect official information about the organization.

2. Add an entry to `directory.json` via PR into this repository.


### Update the HTTPS Everywehere Ruleset

Update the HTTPS Everywhere Ruleset by using the `update-ruleset.py` script:

```
python update-ruleset.py
```

This populates the `rulesets` directory. Inspect them and check all looks sane.

To sign the rules, see HTTPS Everywhere docs [here](https://github.com/EFForg/https-everywhere/blob/master/docs/en_US/ruleset-update-channels.md#2-signing-rulesets-with-this-key) for the signing process. In the step where you remove all HTTPS Everywhere rules from `rules` in the git checkout of the `https-everywhere` git repo, you should copy all rules from `rulesets` generated from the above Python script. You do not need to create a trivial rule as described in the HTTPS Everywhere docs.

For the production rules this signing must be done via the official signing ceremony and the existing GL release key.

Once you have the signature, place the files to serve in the root of the git tree in this repository,and then update the directory listing in `index.html`.

Commit the resulting `index.html` and all files to be served.

Upon merge the ruleset release will be live.


### Credits
Code developed by [evilaliv3](https://github.com/evilaliv3) based on original work by [redshiftzero](https://github.com/redshiftzero) @[securedrop](https://github.com/freedomofpress/securedrop)

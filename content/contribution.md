# Contribution Guide

Welcome to the PrimeVue Contribution Guide and thank you for considering contributing.

## Introduction [#](https://primevue.org/contribution/#introduction)

PrimeVue is a popular Vue UI library maintained by PrimeTek, a company renowned for its comprehensive set of UI components for various frameworks. PrimeTek is dedicated to providing high-quality, versatile, and accessible UI components that help developers build better applications faster.

### Development Setup

To begin with, clone the PrimeVue repository from GitHub:

```

git clone https://github.com/primefaces/primevue.git
cd primevue


```

Then run the showcase in your local environment at *http://localhost:3000/*.

```

npm run setup
npm run dev


```

### Project Structure

PrimeVue utilizes a monorepo architecture, the libraries are located at *packages* folder and the website is at *apps/showcase*.

```

- apps
  - showcase                // website
- packages
  - auto-import-resolver    // unplugin resolver
  - core                    // core api
  - icons                   // primeicons as sfc
  - metadata                // list of components and directives
  - nuxt-module             // module for nuxt    
  - primevue                // main package of components and directives
  - themes                  // presets of styled mode


```

## Help Needed [#](https://primevue.org/contribution/#helpneeded)

PrimeVue is a community-driven project backed by the expertise and sponsorship of PrimeTek, and we appreciate any help you can provide. Here are some areas where you can contribute:

### Issue Triage

Help us manage issues by;

* Reproducing reported bugs
* Clarifying issue descriptions
* Tagging issues with appropriate labels

### Sending Pull Requests

We encourage you to send pull requests, especially for issues tagged with the *help-needed* label.

### Community Support

Assist other users by participating in the issue tracker, [GitHub discussions](https://github.com/orgs/primefaces/discussions/categories/primevue), and the [PrimeLand Discord](https://primevue.org/PrimeLand) server. Your expertise can help others solve problems and improve their experience with PrimeVue.

## Key Points [#](https://primevue.org/contribution/#keypoints)

PrimeVue has several add-ons such as UI Kit, Premium Templates, and Blocks that rely on design tokens and styling. Any core structural changes, such as adding new props, events, or updating design tokens, should be communicated with the core team to ensure consistency and compatibility.

## Communication [#](https://primevue.org/contribution/#communication)

Join the Contributors channel on the [PrimeLand Discord](https://primevue.org/PrimeLand) server to connect with PrimeVue staff and fellow contributors. In this channel, you can discuss the areas you want to contribute to and receive feedback. This channel is open to everyone who'd like to contribute.

## Pathway [#](https://primevue.org/contribution/#pathway)

PrimeTek offers an organization structure involving contributors and the core team:

### Contributor Role

After a certain period of frequent contributions, a community member is offered the Contributor role. On average, it may take about three months, but the exact duration can vary depending on the individual commitment.

### Committer Role

If a contributor actively participates in the codebase and PRs, their role may be upgraded to a Committer level, providing direct commit access to the PrimeVue codebase.

### Employment

PrimeTek prefers to hire team members from open source committers, so you may be offered a full-time position when a position becomes available.

## Benefits [#](https://primevue.org/contribution/#benefits)

Contributing to PrimeVue comes with several benefits. Being part of an open-source project will enhance your career and open up exciting opportunities. Contributors and Committers will be listed on our [team page](https://primevue.org/team). You'll gain significant visibility in the developer community while improving yourself as a professional.

You'll be invited to a private communication channel at Discord to get in touch with PrimeTek. In addition, contributors have access to all PrimeVue add-ons like Premium Templates, Blocks, and UI Kit free of charge.

## CLA [#](https://primevue.org/contribution/#cla)

When a community member is offered the Contributor role, they are expected to sign a Contributor License Agreement (CLA) for legal purposes. This helps protect both the contributor and PrimeTek.
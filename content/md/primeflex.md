# Introduction

The PrimeFlex CSS library is being sunset and will no longer receive active development or maintenance.

## Overview [#](https://primevue.org/guides/primeflex/#overview)

[PrimeFlex](https://primeflex.org) is designed to be a lightweight CSS utility to accompany Prime UI libraries. As part of our product roadmap planning at PrimeTek, the team has decided to avoid the maintenance of a CSS library and utilize the resources on improving the UI libraries instead. Community feedback has been essential in this decision as well since majority of the applications have their own CSS utilities whether it is Tailwind, Bootstrap or an in-house one, as a result adding PrimeFlex to a project was causing overlapping functionality.

## Compatibility [#](https://primevue.org/guides/primeflex/#compatibility)

The compatible versions to choose the correct combination.

|  |  |
| --- | --- |
| PrimeVue v4 and newer | PrimeFlex v4 |
| PrimeVue v3 and older | PrimeFlex v3 |

## Tailwind CSS [#](https://primevue.org/guides/primeflex/#tailwindcss)

Tailwind CSS in particular is a popular choice, we have even built the [Volt UI](https://volt.primevue.org) library spin-off project for the unstyled mode to be able to use the utility classes to style the PrimeVue components. During this work, we've realized that the value added by PrimeFlex such as providing the PrimeVue theming as utility classes can be implemented as a Tailwind plugin. As part of PrimeVue v4, a tailwind-primeui plugin has been created for the seamless integration, the website templating demos have been migrated from PrimeFlex to Tailwind and a converter tool called *pf2tw* has been created. In summary, PrimeTek officially suggests Tailwind CSS as the replacement for PrimeFlex.

## Plugin [#](https://primevue.org/guides/primeflex/#plugin)

The [tailwindcss-primeui](https://www.npmjs.com/package/tailwindcss-primeui) is an official plugin by PrimeTek to provide first class integration between a Prime UI library like PrimeVue and Tailwind CSS. It is designed to work both in styled and unstyled modes. For example, in styled mode the semantic colors such as primary and surfaces are provided as Tailwind utilities e.g. *bg-primary*, *text-surface-500*, *text-muted-color* by deriving their values from the design tokens. This integration is not compatible with PrimeVue v3 and requires PrimeVue v4.

View the [Tailwind](https://primevue.org/tailwind/) section for more details about how to use Tailwind CSS with PrimeVue efficiently.

## Migration [#](https://primevue.org/guides/primeflex/#migration)

The [primeclt](https://www.npmjs.com/package/primeclt) is a command line utility by PrimeTek to assist project setup and migration. The *pf2tw* command is created for smooth migration between PrimeFlex to Tailwind CSS. As a prequisite, the *tailwindcss-primeui* is required to provide the matching classes that do not exist in core Tailwind CSS such as semantic colors and animations. For flawless migration, it is highly suggested to use PrimeVue v4 as the requirement of the tailwindcss plugin.

Install PrimeCLT.

```

npm install -g primeclt


```

Run the *pf2tw* in a directory that contains files to be migrated.

```

prime pf2tw


```

There are a couple of utility classes that are not migrated as they have no counterparts, use flexbox utilities instead as replacements.

* formgrid
* formgroup
* formgroup-inline
* col
* col-fixed
* field
* field-checkbox
* field-radiobutton
* reset
# KeyFilter

A keyfilter is a directive used to block individual keystrokes based on a pattern.

## Import [#](https://primevue.org/keyfilter/#import)

```

import KeyFilter from 'primevue/keyfilter';

app.directive('keyfilter', KeyFilter);


```

## Presets [#](https://primevue.org/keyfilter/#presets)

KeyFilter provides various presets configured with the *v-keyfilter* directive.

Integer

Number

Money

Hex

Alphabetic

Alphanumeric

```

<InputText v-keyfilter.int />
<InputText v-keyfilter.num />
<InputText v-keyfilter.money />
<InputText v-keyfilter.hex />
<InputText v-keyfilter.alpha />
<InputText v-keyfilter.alphanum />


```

## Regex (Single Keypress) [#](https://primevue.org/keyfilter/#regex)

In addition to the presets, a regular expression can be configured for customization of blocking a single key press.

Block Space

Block < > \* !

```

<InputText v-model="spacekey" v-keyfilter="/[^s]/" />
<InputText v-model="chars" v-keyfilter="/^[^<>*!]+$/" />


```

## Regex (Whole Word) [#](https://primevue.org/keyfilter/#regexword)

In addition to the presets, a regular expression can be used to validate the entire word using *validateOnly* option.

Block Numeric (allow "+" only once at start)

```

<InputText v-model="text" v-keyfilter="{ pattern: /^[+]?(d{1,12})?$/, validateOnly: true }" />


```

## Accessibility [#](https://primevue.org/keyfilter/#accessibility)

KeyFilter is a directive and do not require any accessibility features.
# ProgressBar

ProgressBar is a process status indicator.

## Import [#](https://primevue.org/progressbar/#import)

```

import ProgressBar from 'primevue/progressbar';


```

## Basic [#](https://primevue.org/progressbar/#basic)

ProgressBar is used with the *value* property.

50%

```

<ProgressBar :value="50"></ProgressBar>


```

## Dynamic [#](https://primevue.org/progressbar/#dynamic)

Value is reactive so updating it dynamically changes the bar as well.

```

<ProgressBar :value="value"></ProgressBar>


```

## Template [#](https://primevue.org/progressbar/#template)

Custom content inside the ProgressBar is defined with the *default* slot.

40/100

```

<ProgressBar :value="40"> {{ value }}/100 </ProgressBar>


```

## Indeterminate [#](https://primevue.org/progressbar/#indeterminate)

For progresses with no value to track, set the *mode* property to *indeterminate*.

```

<ProgressBar mode="indeterminate" style="height: 6px"></ProgressBar>


```

## Accessibility [#](https://primevue.org/progressbar/#accessibility)

### Screen Reader

ProgressBar components uses *progressbar* role along with *aria-valuemin*, *aria-valuemax* and *aria-valuenow* attributes. Value to describe the component can be defined using *aria-labelledby* and *aria-label* props.

```

<span id="label_status" />
<ProgressBar aria-labelledby="label_status" />

<ProgressBar aria-label="Status" />


```

### Keyboard Support

Not applicable.
# ProgressSpinner

ProgressSpinner is a process status indicator.

## Import [#](https://primevue.org/progressspinner/#import)

```

import ProgressSpinner from 'primevue/progressspinner';


```

## Basic [#](https://primevue.org/progressspinner/#basic)

An infinite spin animation is displayed by default.

```

<ProgressSpinner />


```

## Custom [#](https://primevue.org/progressspinner/#custom)

ProgressSpinner can be customized with styling property like *style*, *strokeWidth* *fill* and *animationDuration*.

```

<ProgressSpinner style="width: 50px; height: 50px" strokeWidth="8" fill="transparent"
    animationDuration=".5s" aria-label="Custom ProgressSpinner" />


```

## Accessibility [#](https://primevue.org/progressspinner/#accessibility)

### Screen Reader

ProgressSpinner components uses *progressbar* role. Value to describe the component can be defined using *aria-labelledby* and *aria-label* props.

```

<ProgressSpinner aria-label="Loading" />


```

### Keyboard Support

Component does not include any interactive elements.
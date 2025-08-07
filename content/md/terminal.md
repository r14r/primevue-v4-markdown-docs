# Terminal

Terminal is a text based user interface.

## Import [#](https://primevue.org/terminal/#import)

```

import Terminal from 'primevue/terminal';
import TerminalService from 'primevue/terminalservice'


```

## Basic [#](https://primevue.org/terminal/#basic)

Commands are processed using an EventBus implementation called *TerminalService*. Import this service into your component and subscribe to the *command* event to process the commands by sending replies with the *response* event.

Enter "**date**" to display the current date, "**greet {0}**" for a message and "**random**" to get a random number.

Welcome to PrimeVue

primevue $

```

<Terminal
    welcomeMessage="Welcome to PrimeVue"
    prompt="primevue $"
    aria-label="PrimeVue Terminal Service"
/>


```

## Accessibility [#](https://primevue.org/terminal/#accessibility)

### Screen Reader

Terminal component has an input element that can be described with *aria-label* or *aria-labelledby* props. The element that lists the previous commands has *aria-live* so that changes are received by the screen reader.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus through the input element. |
| *enter* | Executes the command when focus in on the input element. |
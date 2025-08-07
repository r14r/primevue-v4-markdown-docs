# Accessibility

PrimeVue has WCAG 2.1 AA level compliance, refer to the accessibility documentation of each component for detailed information.

## Introduction [#](https://primevue.org/guides/accessibility/#introduction)

According to the World Health Organization, 15% of the world population has a disability to some degree. As a result, accessibility features in any context such as a ramp for wheelchair users or a multimedia with captions are crucial to ensure content can be consumed by anyone.

Types of disabilities are diverse so you need to know your audience well and how they interact with the content created. There four main categories;

### Visual Impairments

Blindness, low-level vision or color blindness are the common types of visual impairments. Screen magnifiers and the color blind mode are usually built-in features of the browsers whereas for people who rely on screen readers, page developers are required to make sure content is readable by the readers. Popular readers are  [NVDA](https://www.nvaccess.org)  ,  [JAWS](https://www.freedomscientific.com/Products/software/JAWS/)  and  [ChromeVox](https://www.chromevox.com)  .

### Hearing Impairments

Deafness or hearing loss refers to the inability to hear sounds totally or partially. People with hearing impairments use assistive devices however it may not be enough when interacting with a web page. Common implementation is providing textual alternatives, transcripts and captions for content with audio.

### Mobility Impairments

People with mobility impairments have disabilities related to movement due to loss of a limb, paralysis or other varying reasons. Assistive technologies like a head pointer is a device to interact with a screen whereas keyboard or a trackpad remain as solutions for people who are not able to utilize a mouse.

### Cognitive Impairments

Cognitive impairments have a wider range that includes people with learning disabilities, depression and dyslexia. A well designed content also leads to better user experience for people without disabilities so designing for cognitive impairments result in better design for any user.

## WCAG [#](https://primevue.org/guides/accessibility/#wcag)

Correct page structure with the aid of assistive technologies are the core ingridients for an accessible web content. HTML is based on an accessible foundation, form controls can be used by keyboard by default and semantic HTML is easier to be processed by a screen reader.

[WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)  refers to **Web Content Accessibility Guideline**, a standard managed by the WAI (Web Accessibility Initiative) of W3C (World Wide Web Consortium). WCAG consists of recommendations for making the web content more accessible. PrimeVue components aim high level of WCAG compliancy in the near future.

Various countries around the globe have governmental policies regarding web accessibility as well. Most well known of these are [Section 508](https://www.section508.gov/manage/laws-and-policies/) in the US and [Web Accessibility Directive](https://digital-strategy.ec.europa.eu/en/policies/web-accessibility) of the European Union.

## Form Controls [#](https://primevue.org/guides/accessibility/#formcontrols)

Native form elements should be preferred instead of elements that are meant for other purposes like presentation. As an example, button below is rendered as a form control by the browser, can receive focus via tabbing and can be used with space key as well to trigger.

```

<button @click="onButtonClick(event)">Click</button>
        

```

On the other hand, a fancy css based button using a div has no keyboard or screen reader support.

```

<div class="fancy-button" @click="onButtonClick(event)">Click</div>


```

*tabindex* is required to make a div element accessible in addition to use a keydown to bring the keyboard support back. To avoid the overload and implementing functionality that is already provided by the browser, native form controls should be preferred.

```

<div class="fancy-button" @click="onClick(event)" @keydown="onKeyDown(event)" tabindex="0">Click</div>


```

Form components must be related to another element that describes what the form element is used for. This is usually achieved with the *label* element.

```

<label for="myinput">Username:</label>
<input id="myinput" type="text" name="username" />


```

## Semantic HTML [#](https://primevue.org/guides/accessibility/#semantichtml)

HTML offers various element to organize content on a web page that screen readers are aware of. Preferring Semantic HTML for good semantics provide out of the box support for reader which is not possible when regular *div* elements with classes are used. Consider the following example that do not mean too much for readers.

```

<div class="header">
    <div class="header-text">Header</div>
</div>

<div class="nav"></div>

<div class="main">
    <div class="content">
    </div>

    <div class="sidebar">
    </div>
</div>

<div class="footer">
</div>


```

Same layout can be achieved using the semantic elements with screen reader support built-in.

```

<header>
    <h1>Header</h1>
</header>

<nav></nav>

<main>
    <article></article>

    <aside></aside>
</main>

<footer>
</footer>


```

## WAI ARIA [#](https://primevue.org/guides/accessibility/#waiaria)

ARIA refers to "Accessible Rich Internet Applications" is a suite to fill the gap where semantic HTML is inadequate. These cases are mainly related to rich UI components/widgets. Although browser support for rich UI components such as a datepicker or colorpicker has been improved over the past years many web developers still utilize UI components derived from standard HTML elements created by them or by other projects like PrimeVue. These types of components must provide keyboard and screen reader support, the latter case is where the WAI-ARIA is utilized.

ARIA consists of roles, properties and attributes. **Roles** define what the element is mainly used for e.g. *checkbox*, *dialog*, *tablist* whereas **States** and **Properties** define the metadata of the element like *aria-checked*, *aria-disabled*.

Consider the following case of a native checkbox. It has built-in keyboard and screen reader support.

```

<input type="checkbox" value="Prime" name="ui" checked>


```

A fancy checkbox with css animations might look more appealing but accessibility might be lacking. Checkbox below may display a checked font icon with animations however it is not tabbable, cannot be checked with space key and cannot be read by a reader.

```

<div class="fancy-checkbox">
    <i class="checked-icon" v-if="checked"></i>
</div>


```

One alternative is using ARIA roles for readers and use javascript for keyboard support. Notice the usage of *aria-labelledby* as a replacement of the *label* tag with for.

```

<span id="chk-label">Remember Me</span>
<div class="fancy-checkbox" role="checkbox" aria-checked="false" tabindex="0" aria-labelledby="chk-label"
    @click="toggle" @keydown="onKeyDown(event)">
    <i class="checked-icon" v-if="checked"></i>
</div>


```

However the best practice is combining semantic HTML for accessibility while keeping the design for UX. This approach involves hiding a native checkbox for accessibility and using javascript events to update its state. Notice the usage of *p-hidden-accessible* that hides the elements from the user but not from the screen reader.

```

<label for="chkbox">Remember Me</label>
<div class="fancy-checkbox" @click="toggle">
    <input class="p-hidden-accessible" type="checkbox" id="chkbox" @focus="updateParentVisuals" @blur="updateParentVisuals"
        @keydown="onKeyDown(event)">
    <i class="checked-icon" v-if="checked"></i>
</div>


```

A working sample is the PrimeVue checkbox that is tabbable, keyboard accessible and is compliant with a screen reader. Instead of ARIA roles it relies on a hidden native checkbox.

Remember Me

## Colors [#](https://primevue.org/guides/accessibility/#colors)

Colors on a web page should aim a contrast ratio of at least **4.5:1** and consider a selection of colors that do not cause vibration.

### Good Contrast

Color contrast between the background and the foreground content should be sufficient enough to ensure readability. Example below displays two cases with good and bad samples.

GOOD

BAD

### Vibration

Color vibration is leads to an illusion of motion due to choosing colors that have low visibility against each other. Color combinations need to be picked with caution to avoid vibration.

VIBRATE

### Dark Mode

Highly saturated colors should be avoided when used within a dark design scheme as they cause eye strain. Instead desaturated colors should be preferred.

Indigo 500

Indigo 200
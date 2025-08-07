# Stepper

The Stepper component displays a wizard-like workflow by guiding users through the multi-step progression.

## Import [#](https://primevue.org/stepper/#import)

```

import Stepper from 'primevue/stepper';
import StepList from 'primevue/steplist';
import StepPanels from 'primevue/steppanels';
import StepItem from 'primevue/stepitem';
import Step from 'primevue/step';
import StepPanel from 'primevue/steppanel';


```

## Horizontal [#](https://primevue.org/stepper/#horizontal)

Stepper consists of a combination of *StepList*, *Step*, *StepPanels* and *StepPanel* components. The *value* property is essential for associating Step and StepPanel with each other.

1Header I

2Header II

3Header III

Content I

Next

Content II

BackNext

Content III

Back

```

<Stepper value="1">
    <StepList>
        <Step value="1">Header I</Step>
        <Step value="2">Header II</Step>
        <Step value="3">Header III</Step>
    </StepList>
    <StepPanels>
        <StepPanel v-slot="{ activateCallback }" value="1">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content I</div>
            </div>
            <div class="flex pt-6 justify-end">
                <Button label="Next" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback('2')" />
            </div>
        </StepPanel>
        <StepPanel v-slot="{ activateCallback }" value="2">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content II</div>
            </div>
            <div class="flex pt-6 justify-between">
                <Button label="Back" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('1')" />
                <Button label="Next" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback('3')" />
            </div>
        </StepPanel>
        <StepPanel v-slot="{ activateCallback }" value="3">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content III</div>
            </div>
            <div class="pt-6">
                <Button label="Back" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('2')" />
            </div>
        </StepPanel>
    </StepPanels>
</Stepper>


```

## Vertical [#](https://primevue.org/stepper/#vertical)

Vertical layout requires *StepItem* as a wrapper of *Step* and *StepPanel* components.

1Header I

Content I

Next

2Header II

Content II

BackNext

3Header III

Content III

Back

```

<Stepper value="1">
    <StepItem value="1">
        <Step>Header I</Step>
        <StepPanel v-slot="{ activateCallback }">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content I</div>
            </div>
             <div class="py-6">
                <Button label="Next" @click="activateCallback('2')" />
            </div>
        </StepPanel>
    </StepItem>
    <StepItem value="2">
        <Step>Header II</Step>
        <StepPanel v-slot="{ activateCallback }">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content II</div>
            </div>
            <div class="flex py-6 gap-2">
                <Button label="Back" severity="secondary" @click="activateCallback('1')" />
                <Button label="Next" @click="activateCallback('3')" />
            </div>
        </StepPanel>
    </StepItem>
    <StepItem value="3">
        <Step>Header III</Step>
        <StepPanel v-slot="{ activateCallback }">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content III</div>
            </div>
             <div class="py-6">
                <Button label="Back" severity="secondary" @click="activateCallback('2')" />
            </div>
        </StepPanel>
    </StepItem>
</Stepper>


```

## Linear [#](https://primevue.org/stepper/#linear)

When *linear* property is present, current step must be completed in order to move to the next step.

1Header I

2Header II

3Header III

Content I

Next

Content II

BackNext

Content III

Back

```

<Stepper value="1" linear>
    <StepList>
        <Step value="1">Header I</Step>
        <Step value="2">Header II</Step>
        <Step value="3">Header III</Step>
    </StepList>
    <StepPanels>
        <StepPanel v-slot="{ activateCallback }" value="1">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content I</div>
            </div>
            <div class="flex pt-6 justify-end">
                <Button label="Next" icon="pi pi-arrow-right" @click="activateCallback('2')" />
            </div>
        </StepPanel>
        <StepPanel v-slot="{ activateCallback }" value="2">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content II</div>
            </div>
            <div class="flex pt-6 justify-between">
                <Button label="Back" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('1')" />
                <Button label="Next" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback('3')" />
            </div>
        </StepPanel>
        <StepPanel v-slot="{ activateCallback }" value="3">
            <div class="flex flex-col h-48">
                <div class="border-2 border-dashed border-surface-200 dark:border-surface-700 rounded bg-surface-50 dark:bg-surface-950 flex-auto flex justify-center items-center font-medium">Content III</div>
            </div>
            <div class="pt-6">
                <Button label="Back" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback('2')" />
            </div>
        </StepPanel>
    </StepPanels>
</Stepper>


```

## Steps Only [#](https://primevue.org/stepper/#stepsonly)

Use Stepper with a *StepList* only for custom requirements where a progress indicator is needed.

1Design

2Development

3QA

```

<Stepper value="1" class="basis-[50rem]">
    <StepList>
        <Step value="1">Design</Step>
        <Step value="2">Development</Step>
        <Step value="3">QA</Step>
    </StepList>
</Stepper>


```

## Template [#](https://primevue.org/stepper/#template)

Custom content for a step is defined with the default slot. The optional *as* property controls the default container element of a step, for example setting it to a *button* renders a button for the header instead of a div. The *asChild* option enables the headless mode for further customization by passing callbacks and properties to implement your own step.

Create your account

Next

Choose your interests

NatureArtMusicDesignPhotographyMoviesSportsGamingTravelingDancing

BackNext

Account created successfully

Back

```

<Stepper v-model:value="activeStep" class="basis-[40rem]">
    <StepList>
        <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="1">
            <div class="flex flex-row flex-auto gap-2" v-bind="a11yAttrs.root">
                <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback" v-bind="a11yAttrs.header">
                    <span
                        :class="[
                            'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                            { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                        ]"
                    >
                        <i class="pi pi-user" />
                    </span>
                </button>
                <Divider />
            </div>
        </Step>
        <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="2">
            <div class="flex flex-row flex-auto gap-2 pl-2" v-bind="a11yAttrs.root">
                <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback" v-bind="a11yAttrs.header">
                    <span
                        :class="[
                            'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                            { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                        ]"
                    >
                        <i class="pi pi-star" />
                    </span>
                </button>
                <Divider />
            </div>
        </Step>
        <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="3">
            <div class="flex flex-row pl-2" v-bind="a11yAttrs.root">
                <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback" v-bind="a11yAttrs.header">
                    <span
                        :class="[
                            'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                            { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                        ]"
                    >
                        <i class="pi pi-id-card" />
                    </span>
                </button>
            </div>
        </Step>
    </StepList>
    <StepPanels>
        <StepPanel v-slot="{ activateCallback }" :value="1">
            <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 20rem">
                <div class="text-center mt-4 mb-4 text-xl font-semibold">Create your account</div>
                <div class="field">
                    <InputText id="input" v-model="name" type="text" placeholder="Name" fluid />
                </div>
                <div class="field">
                    <InputText id="email" v-model="email" type="email" placeholder="Email" fluid />
                </div>
                <div class="field">
                    <Password v-model="password" placeholder="Password" fluid />
                </div>
            </div>
            <div class="flex pt-6 justify-end">
                <Button label="Next" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(2)" />
            </div>
        </StepPanel>
        <StepPanel v-slot="{ activateCallback }" :value="2">
            <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 24rem">
                <div class="text-center mt-4 mb-4 text-xl font-semibold">Choose your interests</div>
                <div class="flex flex-wrap justify-center gap-4">
                    <ToggleButton v-model="option1" onLabel="Nature" offLabel="Nature" />
                    <ToggleButton v-model="option2" onLabel="Art" offLabel="Art" />
                    <ToggleButton v-model="option3" onLabel="Music" offLabel="Music" />
                    <ToggleButton v-model="option4" onLabel="Design" offLabel="Design" />
                    <ToggleButton v-model="option5" onLabel="Photography" offLabel="Photography" />
                    <ToggleButton v-model="option6" onLabel="Movies" offLabel="Movies" />
                    <ToggleButton v-model="option7" onLabel="Sports" offLabel="Sports" />
                    <ToggleButton v-model="option8" onLabel="Gaming" offLabel="Gaming" />
                    <ToggleButton v-model="option9" onLabel="Traveling" offLabel="Traveling" />
                    <ToggleButton v-model="option10" onLabel="Dancing" offLabel="Dancing" />
                </div>
            </div>
            <div class="flex pt-6 justify-between">
                <Button label="Back" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback(1)" />
                <Button label="Next" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(3)" />
            </div>
        </StepPanel>
        <StepPanel v-slot="{ activateCallback }" :value="3">
            <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 24rem">
                <div class="text-center mt-4 mb-4 text-xl font-semibold">Account created successfully</div>
                <div class="flex justify-center">
                    <img alt="logo" src="https://primefaces.org/cdn/primevue/images/stepper/content.svg" />
                </div>
            </div>
            <div class="flex pt-6 justify-start">
                <Button label="Back" severity="secondary" icon="pi pi-arrow-left" @click="activateCallback(2)" />
            </div>
        </StepPanel>
    </StepPanels>
</Stepper>


```

## Accessibility [#](https://primevue.org/stepper/#accessibility)

### Screen Reader

Stepper container is defined with the *tablist* role, as any attribute is passed to the container element *aria-labelledby* can be optionally used to specify an element to describe the Stepper. Each stepper header has a *tab* role and *aria-controls* to refer to the corresponding stepper content element. The content element of each stepper has *tabpanel* role, an id to match the *aria-controls* of the header and *aria-labelledby* reference to the header as the accessible name.

### Tab Header Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus through the header. |
| *enter* | Activates the focused stepper header. |
| *space* | Activates the focused stepper header. |
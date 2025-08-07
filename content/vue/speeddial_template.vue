<SpeedDial :model="items" direction="up" :transitionDelay="80" :style="{ position: 'absolute' }" pt:menuitem="m-2">
    <template #button="{ toggleCallback }">
        <Button variant="outlined" class="border" @click="toggleCallback">
            <svg width="35" height="40" viewBox="0 0 35 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="..." fill="var(--p-primary-color)" />
                <path d="..." fill="var(--p-text-color)" />
            </svg>
        </Button>
    </template>
    <template #item="{ item, toggleCallback }">
        <div class="flex flex-col items-center justify-between gap-2 p-2 border rounded border-surface-200 dark:border-surface-700 w-20 cursor-pointer" @click="toggleCallback">
            <span :class="item.icon" />
            <span>
                {{ item.label }}
            </span>
        </div>
    </template>
</SpeedDial>
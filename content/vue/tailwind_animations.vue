<Select v-model="animation" :options="animations" placeholder="Select One" class="w-full sm:w-44" />
<div class="py-8 overflow-hidden">
    <div :class="`rounded-border bg-primary w-16 h-16 mx-auto animate-${animation} animate-once animate-duration-1000`"></div>
</div>
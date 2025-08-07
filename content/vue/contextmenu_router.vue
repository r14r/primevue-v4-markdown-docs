<span class="inline-flex items-center justify-center border-2 border-primary rounded w-16 h-16" @contextmenu="onRightClick" aria-haspopup="true">
    <svg width="35" height="40" viewBox="0 0 35 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="..." fill="var(--p-primary-color)" />
        <path d="..." fill="var(--p-text-color)" />
    </svg>
</span>
<ContextMenu ref="routemenu" :model="items">
    <template #item="{ item, props }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
        </a>
    </template>
</ContextMenu>
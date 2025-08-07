<PanelMenu :model="items">
    <template #item="{ item }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple class="flex items-center cursor-pointer text-surface-700 dark:text-surface-0 px-4 py-2" :href="href" @click="navigate">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else v-ripple class="flex items-center cursor-pointer text-surface-700 dark:text-surface-0 px-4 py-2" :href="item.url" :target="item.target">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
            <span v-if="item.items" class="pi pi-angle-down text-primary ml-auto" />
        </a>
    </template>
</PanelMenu>
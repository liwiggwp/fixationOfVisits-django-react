import { LESSON_ROUTE } from "./utils/consts";
import LessonCard from "./pages/LessonCard"

export const publicRoutes = [
    {
        path: LESSON_ROUTE + '/:id',
        Component: LessonCard
    }
]
import AppBar from '@material-ui/core/AppBar';
import Typography from '@material-ui/core/Typography';
import { withStyles } from "@material-ui/core/styles";
import Grid from '@material-ui/core/Grid';
import { colors } from "../common/helpers";
import uw_chem from "../common/images/uw_chem.png";

const RedTextTypography = withStyles({
    root: {
        color: colors.uw_red
    }
})(Typography);

const styles = {
    background: colors.uw_white,
};

function MainHeader() {
    return (
        <AppBar
            style={styles}
        >
            <Grid container spacing={24}>
                <Grid item xs={6}>
                    <img src={uw_chem} alt={"Chem"} width={700} height={100}/>
                </Grid>
                <Grid item xs={6}>
                    <RedTextTypography
                        variant={'h2'}
                    >
                    Inventory Management
                    </RedTextTypography>
                </Grid>
            </Grid>
        </AppBar>
    )
}

export default MainHeader;